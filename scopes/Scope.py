from .Variable import *

class Scope():
    def __init__(self, parent: "Scope"):
        self.__parent = parent
        self.__variables = dict()

    @property
    def parent(self):
        return self.__parent

    def add_var(self, name, var_type, access_modifier:AccessModifier):
        new_var = Variable(name, var_type, access_modifier)
        self.__variables.update({name, new_var})
    
    def contains_var(self, name):
        return name in self.__variables

    def find_var(self, name):
        if name in self.__variables:
            return self.__variables[name]
        elif self.__parent:
            return self.__parent.find_var(name)
        else:
            return None