from scopes.ClassScope import ClassScope
from uuid import uuid4
from antlr4 import *
import grammar.IdleLexer

class IdleCompiler:
    """Class used to control compilation process."""

    def __init__(self):
        self.__classes = dict()
        self.__current_class = None
        self.__compiler_errors = []
        self.__current_scope = None

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

        # Check existence
        if self.__current_class.contains_func(func_name):
            self.__compiler_errors.append("line %i: Duplicate method name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        # Add function to class and update current_scope
        self.__current_class.add_func(func_name)
        self.__current_scope = self.__current_class.find_func(func_name)
    
    def update_func_type(self, type_name):
        """Called after adding function, updates last function's return type."""

        self.__current_class.update_func_return_type(type_name)

    def check_func_exists(self, func_name, line_num):
        """Checks if a function is available for use in current scope."""
        
        current_class = self.__current_class
        
        while current_class:
            if current_class.contains_func(func_name):
                return
            current_class = current_class.parent_class
        
        self.__compiler_errors.append("line %i: Undeclared function '%s'" % (line_num, func_name))
    
    def add_var(self, var_name, line_num):
        """Adds variable to current scope. Does not allow duplicates.
        
        'commit_vars' should be called afterwards when variable type is known.
        """

        if self.__current_scope.contains_var(var_name):
            self.__compiler_errors.append("line %i: Duplicate var '%s'" % (line_num, var_name))
        else:
            self.__current_scope.add_var(var_name)

    def commit_vars(self, type_name):
        """Commits previously added variables.
        
        To be called after calling 'add_var' and when variable type is known.
        """

        self.__current_scope.commit_vars(type_name)
    
    def end_scope(self):
        """Should be called when scope ended and returns to parent's scope"""

        self.__current_scope = self.__current_scope.parent
    
    def check_var_exists(self, var_name, line_num):
        """Checks if variable is available for use in current scope."""

        if not(self.__current_scope.var_in_scope(var_name)):
            self.__compiler_errors.append("line %i: Undeclared variable '%s'" % (line_num, var_name))

    def check_instance_var_exists(self, var_name, line_num):
        """Checks if an instance variable is available for use in current scope."""
        
        current_class = self.__current_class
        while current_class:
            if current_class.var_in_scope(var_name):
                return
            current_class = current_class.parent_class
        
        self.__compiler_errors.append("line %i: Undeclared instance variable '%s'" % (line_num, var_name))