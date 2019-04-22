from scopes.ClassScope import ClassScope
from scopes.Scope import Scope, AccessModifier
from scopes.Func import Func
from uuid import uuid4
from antlr4 import *
from utils.DataType import DataType
import grammar.IdleLexer
from IdleInterRepr import IdleInterRepr
from scopes.CompilationMemory import CompilationMemory

class IdleCompiler:
    """Class used to control compilation process."""

    # Attributes declared static to be shared in case of imports.
    __classes = dict()
    __current_class = None
    __compiler_errors = []
    __current_scope = None
    __interp = IdleInterRepr()
    __should_gen_quads = True

    # Attributes that should be initialized before initial compilation
    cwd = None # Current working directory
    files_imported = []

    def __init__(self):
        # Generate first quad, jump to main() only for original file, not imported
        if len(IdleCompiler.files_imported) == 1:
            IdleCompiler.__interp.add_goto_main()

    @property
    def compiler_errors(self):
        return IdleCompiler.__compiler_errors
    
    @property
    def classes(self):
        return IdleCompiler.__classes

    @property
    def quads(self):
        return IdleCompiler.__interp.quads
    
    @property
    def const_quads(self):
        return IdleCompiler.__interp.constant_quads()
    
    def set_main(self):
        if IdleCompiler.__should_gen_quads:
            main_func = IdleCompiler.__current_class.find_func('main')
            if main_func != None:
                IdleCompiler.__interp.set_main(main_func)
            else:
                IdleCompiler.__compiler_errors.append("Main method not found.")

    def import_file(self, file_name):
        """Imports a file by starting another nested compilation."""

        # Prevent cyclical or duplicate imports
        if file_name in IdleCompiler.files_imported:
            IdleCompiler.__compiler_errors.append("File '%s' already imported." % file_name)
            return

        print("Importing '%s'..." % file_name)
        IdleCompiler.files_imported.append(file_name)

        # Check for file existence
        file_path = IdleCompiler.cwd + "/" + file_name + ".idle"
        try:
            lexer = grammar.IdleLexer.IdleLexer(FileStream(file_path))
        except:
            IdleCompiler.__compiler_errors.append("File '%s' not found." % file_name)
            return

        # Parse
        stream = CommonTokenStream(lexer)
        parser = grammar.IdleParser.IdleParser(stream)
        tree = parser.fileState()

        # Handle results
        self.handle_import(parser.getNumberOfSyntaxErrors(), file_name)

    def handle_import(self, has_parsing_errors: bool, file_name: str):
        """Adds imported classes to instance or reports if duplicate class name was found."""

        # Remove main method not found error if present, because imported files don't need a main method.
        if len(self.compiler_errors) > 0 and self.compiler_errors[-1] == "Main method not found.":
            self.compiler_errors.pop()
        
        # Look for errors in imported file
        if len(self.compiler_errors) > 0:
            for error in self.compiler_errors:
                print(error) # Print right away for them to go alongisde lexical/syntax errors.
            
            self.compiler_errors.clear()
            IdleCompiler.__compiler_errors.append("Imported file %s has errors." % file_name)
        elif has_parsing_errors:
            IdleCompiler.__compiler_errors.append("Imported file %s has errors." % file_name)

    def add_class(self, class_name, line_num, parent_name=None):
        """Adds a class to symbol table.
        
        If duplicate class name is found, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        # Check existence
        if class_name in IdleCompiler.__classes:
            IdleCompiler.__compiler_errors.append("line %i: Duplicate class '%s'" % (line_num, class_name))
            class_name = class_name + uuid4().hex

        # Check parent existence
        if parent_name and parent_name not in IdleCompiler.__classes:
            IdleCompiler.__compiler_errors.append("line %i: Parent class '%s' not found." % (line_num, parent_name))
            parent_class = None
        else:
            parent_class = IdleCompiler.__classes.get(parent_name, None)
        
        # Add to class table and update current_class and current_scope
        new_class = ClassScope(class_name, parent_class)
        IdleCompiler.__classes[class_name] = new_class
        IdleCompiler.__current_class = new_class
        IdleCompiler.__current_scope = new_class

    def add_func(self, func_name, line_num, access_modifier):
        """Adds a function to symbol table of the last added class.
        
        If duplicate function name is found, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        if IdleCompiler.__current_class.name == func_name:
            IdleCompiler.__compiler_errors.append("line %i: Method name can't be the same as the class name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex

        # Check existence
        if IdleCompiler.__current_class.contains_func(func_name):
            IdleCompiler.__compiler_errors.append("line %i: Duplicate method name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        # Add function to class and update current_scope
        IdleCompiler.__current_class.add_func(func_name, AccessModifier(access_modifier))
        IdleCompiler.__current_scope = IdleCompiler.__current_class.find_func(func_name)
        IdleCompiler.__current_scope.set_func_start(len(self.__interp.quads))
    
    def add_func_return_type(self, return_type):
        """Called after adding function, updates last function's return type."""

        if DataType.exists(return_type):
            return_type = DataType(return_type)
        
        IdleCompiler.__current_scope.return_type = return_type

    def add_constructor(self, func_name, line_num):
        """Adds a constructor to symbol table of the last added class.
        
        If a constructor has already been defined, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        if IdleCompiler.__current_class.name != func_name:
            IdleCompiler.__compiler_errors.append("line %i: Missing return type for method '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex

        # Check existence
        if IdleCompiler.__current_class.contains_func(func_name):
            IdleCompiler.__compiler_errors.append("line %i: Duplicate constructors in '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        # Add function to class and update current_scope
        IdleCompiler.__current_class.add_func(func_name, AccessModifier.PUBLIC)
        IdleCompiler.__current_scope = IdleCompiler.__current_class.find_func(func_name)
        IdleCompiler.__current_scope.return_type = func_name
        IdleCompiler.__current_scope.set_func_start(len(self.__interp.quads))

    def check_func_exists(self, func_name, line_num):
        """Checks if a function is available for use in current scope."""
        
        class_func = IdleCompiler.__current_class.find_func(func_name)
        if class_func != None:
            IdleCompiler.__interp.add_func_era(class_func)
        else:
            IdleCompiler.__compiler_errors.append("line %i: Undeclared function '%s'" % (line_num, func_name))
            IdleCompiler.__should_gen_quads = False
    
    def check_super_func_exists(self, func_name, line_num):
        """Checks if a function is available for use in any parent. Uses first function inherited found."""
        
        parent_class = IdleCompiler.__current_class.parent_class
        if parent_class == None:
            IdleCompiler.__compiler_errors.append("line %i: Class '%s' has no parent." % (line_num, IdleCompiler.__current_class.name))
            IdleCompiler.__should_gen_quads = False
        else:
            super_func = parent_class.find_func(func_name)
            if super_func != None:
                IdleCompiler.__interp.add_func_era(super_func)
            else:
                IdleCompiler.__compiler_errors.append("line %i: Function '%s' not found in parent." % (line_num, func_name))
                IdleCompiler.__should_gen_quads = False

    def check_class_exists(self, class_name, line_num):
        """Checks if a class is available for use in current scope."""
        
        if not class_name in self.classes:
            IdleCompiler.__compiler_errors.append("line %i: Constructor for undefined class '%s'" % (line_num, class_name))
            IdleCompiler.__should_gen_quads = False
        else:
            constructor = self.classes[class_name].find_func(class_name)

            if constructor == None:
                constructor = Func('__default_constructor__')
                constructor.return_type = class_name
            
            IdleCompiler.__interp.add_func_era(constructor)

    def check_obj_func_exists(self, func_name, line_num):
        """Checks if a function exists within the class of var_ref
        
        Assumes undeclared variable error has already been thrown if var_ref doesn't exist.
        """

        var_ref = IdleCompiler.__interp.get_last_var()
        type_name = var_ref.var_type

        if DataType.exists(type_name):
            IdleCompiler.__compiler_errors.append("line %i: Function '%s' not found in '%s'." % (line_num, func_name, type_name))
            IdleCompiler.__should_gen_quads = False
        else:
            class_obj = IdleCompiler.__classes.get(type_name, None)
            
            if class_obj != None:
                class_func = class_obj.find_func(func_name)

            if class_obj != None and class_func != None:
                if class_func.access_modifier == AccessModifier.PUBLIC:
                    IdleCompiler.__interp.add_func_era(class_func, var_ref)
                else:
                    IdleCompiler.__compiler_errors.append("line %i: Function '%s' is a private member of '%s'." % (line_num, func_name, class_obj.name))
                    IdleCompiler.__should_gen_quads = False
            else:
                IdleCompiler.__compiler_errors.append("line %i: Function '%s' not found in '%s'." % (line_num, func_name, type_name))
                IdleCompiler.__should_gen_quads = False

    
    def add_var(self, var_name, line_num):
        """Adds variable to current scope. Does not allow duplicates.
        
        'commit_vars' should be called afterwards when variable type is known.
        """

        if IdleCompiler.__current_scope.contains_var(var_name):
            IdleCompiler.__compiler_errors.append("line %i: Duplicate var '%s'" % (line_num, var_name))
        else:
            IdleCompiler.__current_scope.add_var(var_name)
    
    def add_arg(self, arg_name):
        """Adds a variable as an argument for the current function.
        """
        
        IdleCompiler.__current_scope.add_arg(arg_name)
    
    def param_to_ref(self, arg_name):
        """Sets a previously added argument to be copied by reference and not value."""

        IdleCompiler.__current_scope.change_param_to_ref(arg_name)

    def commit_vars(self, type_name, line_num):
        """Checks type exists and commits previously added variables.
        
        To be called after calling 'add_var' and when variable type is known.
        """

        if DataType.exists(type_name):
            type_name = DataType(type_name)
        elif type_name not in IdleCompiler.__classes:
            IdleCompiler.__compiler_errors.append("line %i: Type '%s' does not exist." % (line_num, type_name))

        IdleCompiler.__current_scope.commit_vars(type_name)
    
    def start_scope(self):
        """Should be called when a new scope begins"""
        IdleCompiler.__current_scope = Scope(None, self.__current_scope)
    
    def end_scope(self):
        """Should be called when scope ended and returns to parent's scope"""

        IdleCompiler.__current_scope = self.__current_scope.parent
    
    def check_var_exists(self, var_name, line_num):
        """Checks if variable is available for use in current scope."""

        if not(IdleCompiler.__current_scope.var_in_scope(var_name)):
            IdleCompiler.__compiler_errors.append("line %i: Undeclared variable '%s'" % (line_num, var_name))
            IdleCompiler.__should_gen_quads = False
        
        var = IdleCompiler.__current_scope.find_var(var_name)
        self.quad_add_var(var)
        return var

    def check_instance_var_exists(self, var_name, line_num):
        """Checks if an instance variable is available for use in current scope."""
        
        var = IdleCompiler.__current_class.find_instance_var(var_name)
        if var != None:
            self.quad_add_var(var)
            return var
        
        IdleCompiler.__should_gen_quads = False
        IdleCompiler.__compiler_errors.append("line %i: Undeclared instance variable '%s'" % (line_num, var_name))
                    
    def reset_new_line(self):
        """If there was previously an error, resets quads to be able to continue compilation.
        
        To be called at end of statement.
        """

        if not IdleCompiler.__should_gen_quads:
            IdleCompiler.__should_gen_quads = True
            IdleCompiler.__interp = IdleInterRepr()

    def add_constant(self, value, var_type):
        var_type = DataType(var_type)

        if var_type == DataType.BOOL:
            value = True if value == 'true' else False
        elif var_type == DataType.FLOAT:
            value = float(value)
        elif var_type == DataType.INT:
            value = int(value)

        const_var = CompilationMemory.get_constant(value, var_type)

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.add_var(const_var)

    def quad_add_var(self, var):
        """Looks for var and adds to quads"""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.add_var(var)
    
    def quad_add_oper(self, oper):
        """Adds operator to quads"""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.add_operator(oper)

    def quad_assign(self, line_num):
        """Adds quad for assignment and reports type mismatch."""

        if IdleCompiler.__should_gen_quads:
            if not IdleCompiler.__interp.assign():
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch" % line_num)
                IdleCompiler.__should_gen_quads = False

    def quad_check_relop(self, line_num):
        """Checks operation and reports type mismatch."""
        
        if IdleCompiler.__should_gen_quads:
            if not IdleCompiler.__interp.check_relop():
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch" % line_num)
                IdleCompiler.__should_gen_quads = False
    
    def quad_check_addsub(self, line_num):
        """Checks operation and reports type mismatch."""

        if IdleCompiler.__should_gen_quads:
            if not IdleCompiler.__interp.check_addsub():
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch" % line_num)
                IdleCompiler.__should_gen_quads = False

    def quad_check_divmult(self, line_num):
        """Checks operation and reports type mismatch."""

        if IdleCompiler.__should_gen_quads:
            if not IdleCompiler.__interp.check_divmult():
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch" % line_num)
                IdleCompiler.__should_gen_quads = False

    def quad_open_parenthesis(self):
        """To be called when opening parenthesis in expression."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.open_parenthesis()
        
    def quad_close_parenthesis(self):
        """To be called when closing parenthesis in expression."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.close_parenthesis()

    def quad_read(self, read_type):
        """Adds quad for read"""

        if IdleCompiler.__should_gen_quads:
            read_type = DataType(read_type)
            IdleCompiler.__interp.read(read_type)

    def quad_print_st(self):
        """Adds quad for read"""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.print_st()

    def quad_start_while(self):
        """Adds pending jump, to be called before loop expression."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.start_while()

    def quad_end_while_expr(self, line_num):
        """Adds loop jump if false to be solved when loop ends."""

        if IdleCompiler.__should_gen_quads and not IdleCompiler.__interp.end_while_expr():
            IdleCompiler.__compiler_errors.append("line %i: Type mismatch. Expecting bool in while expression." % line_num)
            IdleCompiler.__should_gen_quads = False

    def quad_end_while(self):
        """Adds jump to loop back and completes loop end quad."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.end_while()
    
    def quad_start_for_assign(self):
        """Starts temporal quad generation to append at end of for loop."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.start_for_assign()

    def quad_end_for_assign(self):
        """Ends temporal quad generation to append at end of for loop."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.end_for_assign()
    
    def quad_end_for_block(self):
        """Appends temporal assignment quads to end of for loop."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.end_for_block()

    def quad_end_if_expr(self, line_num):
        """Adds conditional jump when expression evaluates to false."""
        if IdleCompiler.__should_gen_quads and not IdleCompiler.__interp.end_if_expr():
            IdleCompiler.__compiler_errors.append("line %i: Type mismatch. Expecting bool in if expression." % line_num)
            IdleCompiler.__should_gen_quads = False

    def quad_fill_if_end_jumps(self):
        """Fills jumps to the end of the if block block."""
        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.fill_if_end_jumps()
    
    def quad_start_else_ifs(self):
        """Generates a stack that will be used to store the quads that will jump to the end of the if block."""
        
        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.start_else_ifs()

    def quad_add_else(self):
        """Fills the GOTOF from the previous if/elseif and adds a GOTO to the end of the if block."""

        if IdleCompiler.__should_gen_quads:
            IdleCompiler.__interp.add_else()

    def quad_add_func_param(self, line_num):
        """To be called for each argument when calling a function. Checks number of parameters and type matching."""

        if IdleCompiler.__should_gen_quads:
            quad_result = IdleCompiler.__interp.add_func_param()
            if not quad_result[0]:
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch. Expecting type %s for parameter %s." % 
                        (line_num, quad_result[2], quad_result[1]))

    def quad_add_func_gosub(self, line_num):
        """Adds quad for jumping to function when called. Expects to be called at end of function call."""

        if IdleCompiler.__should_gen_quads:
            quad_result = IdleCompiler.__interp.add_func_gosub()
            if not quad_result[0]:
                IdleCompiler.__compiler_errors.append("line %i: Wrong number of arguments for function %s, expecting %i but received %i." % 
                    (line_num, quad_result[1], quad_result[2], quad_result[3]))

    def quad_add_func_return(self, line_num):
        """Adds quad for return statement."""

        current_scope = IdleCompiler.__current_scope
        while not isinstance(current_scope, Func):
            current_scope = current_scope.parent
        if IdleCompiler.__should_gen_quads and not IdleCompiler.__interp.add_func_return(current_scope.return_type):
            if current_scope.return_type != None:
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch. Function return type should be %s." % 
                    (line_num, current_scope.return_type))
            else:
                IdleCompiler.__compiler_errors.append("line %i: Type mismatch. Function is void, should not return anything." % line_num)

    def quad_add_endproc(self, line_num):
        """Defines the end of a function. Expects to be called at end of block."""

        if IdleCompiler.__should_gen_quads and not IdleCompiler.__interp.add_endproc(IdleCompiler.__current_scope):
            IdleCompiler.__compiler_errors.append("line %i: Missing return statement. Function return type should be %s." % 
                (line_num, IdleCompiler.__current_scope.return_type))

    def check_not_void(self, line_num, check):
        """Checks that a function called within an expression is not void"""

        if IdleCompiler.__should_gen_quads:
            if not IdleCompiler.__interp.check_not_void(check):
                IdleCompiler.__compiler_errors.append("line %i: Expecting expression with value, but called void function instead." % line_num)
                self.__should_gen_quads = False