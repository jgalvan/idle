from scopes.ClassScope import ClassScope
from uuid import uuid4
from antlr4 import *
import grammar.IdleLexer

class IdleCompiler:
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
        print("Importing '%s'..." % file_name)
        file_name = file_name + ".idle"
        try:
            lexer = grammar.IdleLexer.IdleLexer(FileStream(file_name))
        except:
            self.__compiler_errors.append("File '%s' not found." % file_name)
            return

        stream = CommonTokenStream(lexer)
        parser = grammar.IdleParser.IdleParser(stream)
        tree = parser.fileState()
        self.merge_import(parser.icomp)

        if len(parser.icomp.compiler_errors) > 0:
            for error in parser.icomp.compiler_errors:
                print(error)
            
            self.__compiler_errors.append("Imported file %s has errors." % file_name)
        
        print()

    def merge_import(self, imp_icomp):
        for class_name, class_obj in imp_icomp.classes.items():
            if class_name in self.__classes:
                self.__compiler_errors.append("Imported duplicate class '%s'" % class_name)
            else:
                self.__classes[class_name] = class_obj

    def add_class(self, class_name, line_num):
        if class_name in self.__classes:
            self.__compiler_errors.append("line %i: Duplicate class '%s'" % (line_num, class_name))
            class_name = class_name + uuid4().hex
        
        new_class = ClassScope(class_name)
        self.__classes[class_name] = new_class
        self.__current_class = new_class
        self.__current_scope = new_class

    def add_func(self, func_name, line_num):
        if self.__current_class.contains_func(func_name):
            self.__compiler_errors.append("line %i: Duplicate method name '%s'" % (line_num, func_name))
            func_name = func_name + uuid4().hex
        
        self.__current_class.add_func(func_name)
        self.__current_scope = self.__current_class.find_func(func_name)
    
    def update_func_type(self, type_name):
        self.__current_class.update_func_return_type(type_name)
    
    def add_var(self, var_name, line_num):
        if self.__current_scope.contains_var(var_name):
            self.__compiler_errors.append("line %i: Duplicate var '%s'" % (line_num, var_name))
        else:
            self.__current_scope.add_var(var_name)

    def commit_vars(self, type_name):
        self.__current_scope.commit_vars(type_name)
    
    def end_scope(self):
        self.__current_scope = self.__current_scope.parent
    
    def check_var_exists(self, var_name, line_num):
        if self.__current_scope.var_in_scope(var_name):
            self.__compiler_errors.append("line %i: Undeclared variable '%s'" % (line_num, var_name))