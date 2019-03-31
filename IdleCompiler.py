from scopes.ClassScope import ClassScope
from uuid import uuid4
from antlr4 import *
from utils.DataType import DataType
import grammar.IdleLexer
from IdleInterRepr import IdleInterRepr

class IdleCompiler:
    """Class used to control compilation process."""

    def __init__(self):
        self.__classes = dict()
        self.__current_class = None
        self.__compiler_errors = []
        self.__current_scope = None
        self.__interp = IdleInterRepr()
        self.__should_gen_quads = True

    @property
    def compiler_errors(self):
        return self.__compiler_errors
    
    @property
    def classes(self):
        return self.__classes

    def import_file(self, file_name):
        """Imports a file by starting another nested compilation."""

        print("Importing '%s'..." % file_name)

        # Check for file existence
        file_name = file_name + ".idle"
        try:
            lexer = grammar.IdleLexer.IdleLexer(FileStream(file_name))
        except:
            self.__compiler_errors.append("File '%s' not found." % file_name)
            return

        # Parse
        stream = CommonTokenStream(lexer)
        parser = grammar.IdleParser.IdleParser(stream)
        tree = parser.fileState()

        # Handle results
        self.merge_import(parser.icomp)
        if len(parser.icomp.compiler_errors) > 0:
            for error in parser.icomp.compiler_errors:
                print(error)
            
            self.__compiler_errors.append("Imported file %s has errors." % file_name)
        
        print()

    def merge_import(self, imp_icomp):
        """Adds imported classes to instance or reports if duplicate class name was found."""

        for class_name, class_obj in imp_icomp.classes.items():
            if class_name in self.__classes:
                self.__compiler_errors.append("Imported duplicate class '%s'" % class_name)
            else:
                self.__classes[class_name] = class_obj

    def add_class(self, class_name, line_num, parent_name=None):
        """Adds a class to symbol table.
        
        If duplicate class name is found, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        # Check existence
        if class_name in self.__classes:
            self.__compiler_errors.append("line %i: Duplicate class '%s'" % (line_num, class_name))
            class_name = class_name + uuid4().hex

        # Check parent existence
        if parent_name and parent_name not in self.__classes:
            self.__compiler_errors.append("line %i: Parent class '%s' not found." % (line_num, parent_name))
            parent_class = None
        else:
            parent_class = self.__classes.get(parent_name, None)
        
        # Add to class table and update current_class and current_scope
        new_class = ClassScope(class_name, parent_class)
        self.__classes[class_name] = new_class
        self.__current_class = new_class
        self.__current_scope = new_class

    def add_func(self, func_name, line_num):
        """Adds a function to symbol table of the last added class.
        
        If duplicate function name is found, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        if self.__current_class.name == func_name:
            self.__compiler_errors.append("line %i: Method name can't be the same as the class name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex

        # Check existence
        if self.__current_class.contains_func(func_name):
            self.__compiler_errors.append("line %i: Duplicate method name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        # Add function to class and update current_scope
        self.__current_class.add_func(func_name)
        self.__current_scope = self.__current_class.find_func(func_name)
    
    def add_func_return_type(self, return_type):
        """Called after adding function, updates last function's return type."""

        if DataType.exists(type_name):
            type_name = DataType(type_name)
        
        self.__current_scope.return_type = return_type

    def add_constructor(self, func_name, line_num):
        """Adds a constructor to symbol table of the last added class.
        
        If a constructor has already been defined, it still saves it but with a UUID to allow 
        the compiling process to continue.
        """

        if self.__current_class.name != func_name:
            self.__compiler_errors.append("line %i: Missing return type for method '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex

        # Check existence
        if self.__current_class.contains_func(func_name):
            self.__compiler_errors.append("line %i: Duplicate constructors in '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        # Add function to class and update current_scope
        self.__current_class.add_func(func_name)
        self.__current_scope = self.__current_class.find_func(func_name)
        self.__current_scope.return_type = func_name

    def check_func_exists(self, func_name, line_num):
        """Checks if a function is available for use in current scope."""
        
        if not self.__current_class.contains_func(func_name):
            self.__compiler_errors.append("line %i: Undeclared function '%s'" % (line_num, func_name))

    def check_class_exists(self, class_name, line_num):
        """Checks if a class is available for use in current scope."""
        
        if not class_name in self.classes:
            self.__compiler_errors.append("line %i: Constructor for undefined class '%s'" % (line_num, class_name))
    
    def add_var(self, var_name, line_num):
        """Adds variable to current scope. Does not allow duplicates.
        
        'commit_vars' should be called afterwards when variable type is known.
        """

        if self.__current_scope.contains_var(var_name):
            self.__compiler_errors.append("line %i: Duplicate var '%s'" % (line_num, var_name))
        else:
            self.__current_scope.add_var(var_name)
    
    def add_arg(self, arg_name):
        """Adds a variable as an argument for the current function.
        """
        self.__current_scope.add_arg(arg_name)

    def commit_vars(self, type_name, line_num):
        """Checks type exists and commits previously added variables.
        
        To be called after calling 'add_var' and when variable type is known.
        """

        if DataType.exists(type_name):
            type_name = DataType(type_name)
        elif type_name not in self.__classes:
            self.__compiler_errors.append("line %i: Type '%s' does not exist." % (line_num, type_name))

        self.__current_scope.commit_vars(type_name)
    
    def end_scope(self):
        """Should be called when scope ended and returns to parent's scope"""

        self.__current_scope = self.__current_scope.parent
    
    def check_var_exists(self, var_name, line_num):
        """Checks if variable is available for use in current scope."""

        if not(self.__current_scope.var_in_scope(var_name)):
            self.__compiler_errors.append("line %i: Undeclared variable '%s'" % (line_num, var_name))
            self.__should_gen_quads = False
        
        return self.__current_scope.find_var(var_name)

    def check_instance_var_exists(self, var_name, line_num):
        """Checks if an instance variable is available for use in current scope."""
        
        current_class = self.__current_class
        while current_class:
            if current_class.var_in_scope(var_name):
                return current_class.find_var(var_name)
            current_class = current_class.parent_class
        
        self.__should_gen_quads = False
        self.__compiler_errors.append("line %i: Undeclared instance variable '%s'" % (line_num, var_name))

    def check_obj_func_exists(self, var_ref, func_name, line_num):
        """Checks if a function exists within the class of var_ref
        
        Assumes undeclared variable error has already been thrown if var_ref doesn't exist.
        """

        if var_ref:
            type_name = var_ref.var_type
            primitive_data_types = ['bool', 'int', 'float', 'string']

            if type_name in primitive_data_types:
                self.__compiler_errors.append("line %i: Function '%s' not found in '%s'." % (line_num, func_name, type_name))
            else:
                class_obj = self.__classes[type_name]

                if not class_obj.contains_func(func_name):
                    self.__compiler_errors.append("line %i: Function '%s' not found in '%s'." % (line_num, func_name, type_name))

    def reset_new_line(self):
        """If there was previously an error, resets quads to be able to continue compilation.
        
        To be called at end of statement.
        """

        if not self.__should_gen_quads:
            self.__should_gen_quads = True
            self.__interp = IdleInterRepr()

    def quad_add_var(self, var_name):
        """Looks for var and adds to quads"""

        if self.__should_gen_quads:
            var = self.__current_scope.find_var(var_name)
            self.__interp.add_var(var)
    
    def quad_add_oper(self, oper):
        """Adds operator to quads"""

        if self.__should_gen_quads:
            self.__interp.add_operator(oper)

    def quad_assign(self, var_name, line_num):
        """Adds quad for assignment and reports type mismatch."""

        if self.__should_gen_quads:
            var = self.__current_scope.find_var(var_name)

            if not self.__interp.assign(var):
                self.__compiler_errors.append("line %i: Type mismatch" % line_num)
                self.__should_gen_quads = False

    def quad_check_relop(self, line_num):
        """Checks operation and reports type mismatch."""
        
        if self.__should_gen_quads:
            if not self.__interp.check_relop():
                self.__compiler_errors.append("line %i: Type mismatch" % line_num)
                self.__should_gen_quads = False
    
    def quad_check_addsub(self, line_num):
        """Checks operation and reports type mismatch."""

        if self.__should_gen_quads:
            if not self.__interp.check_addsub():
                self.__compiler_errors.append("line %i: Type mismatch" % line_num)
                self.__should_gen_quads = False

    def quad_check_divmult(self, line_num):
        """Checks operation and reports type mismatch."""

        if self.__should_gen_quads:
            if not self.__interp.check_divmult():
                self.__compiler_errors.append("line %i: Type mismatch" % line_num)
                self.__should_gen_quads = False

    def quad_open_parenthesis(self):
        """To be called when opening parenthesis in expression."""

        if self.__should_gen_quads:
            self.__interp.open_parenthesis()
        
    def quad_close_parenthesis(self):
        """To be called when closing parenthesis in expression."""

        if self.__should_gen_quads:
            self.__interp.close_parenthesis()

    def quad_read(self, read_type):
        """Adds quad for read"""

        if self.__should_gen_quads:
            read_type = DataType(read_type)
            self.__interp.read(read_type)

    def quad_print_st(self):
        """Adds quad for read"""

        if self.__should_gen_quads:
            self.__interp.print_st()

    def quad_start_while(self):
        """Adds pending jump, to be called before loop expression."""

        if self.__should_gen_quads:
            self.__interp.start_while()

    def quad_end_while_expr(self, line_num):
        """Adds loop jump if false to be solved when loop ends."""

        if self.__should_gen_quads and not self.__interp.end_while_expr():
            self.__compiler_errors.append("line %i: Type mismatch. Expecting bool in while expression." % line_num)
            self.__should_gen_quads = False

    def quad_end_while(self):
        """Adds jump to loop back and completes loop end quad."""

        if self.__should_gen_quads:
            self.__interp.end_while()
    
    def quad_start_for_assign(self):
        """Starts temporal quad generation to append at end of for loop."""

        if self.__should_gen_quads:
            self.__interp.start_for_assign()

    def quad_end_for_assign(self):
        """Ends temporal quad generation to append at end of for loop."""

        if self.__should_gen_quads:
            self.__interp.end_for_assign()
    
    def quad_end_for_block(self):
        """Appends temporal assignment quads to end of for loop."""

        if self.__should_gen_quads:
            self.__interp.end_for_block()

    def printQuads(self):
        for i in range(0,(len(self.__interp.quads))):
            print(i, self.__interp.quads[i])