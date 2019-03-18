from .Variable import *

class Scope():
    def __init__(self, name, parent: "Scope"=None):
        self.__name = name
        self.__parent = parent
        self.__variables = dict()
        self.__pending_variables = []

    @property
    def name(self):
        return self.__name

    @property
    def parent(self):
        return self.__parent
    
    def add_var(self, var_name):
        self.__pending_variables.append(var_name)
    
    def commit_vars(self, type_name):
        for var_name in self.__pending_variables:
            current_var = Variable(var_name, type_name)
            self.__variables[var_name] = current_var
        
        self.__pending_variables.clear()
    
    def contains_var(self, name):
        return name in self.__variables
    
    def var_in_scope(self, name):
        if name in self.__variables:
            return True
        elif self.__parent:
            return self.__parent.find_var(name)
        else:
            return False

    def find_var(self, name):
        if name in self.__variables:
            return self.__variables[name]
        elif self.__parent:
            return self.__parent.find_var(name)
        else:
            return None