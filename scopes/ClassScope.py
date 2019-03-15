from .Scope import Scope, AccessModifier
from .Func import Func

class ClassScope(Scope):
    def __init__(self, parent: Scope):
        self.__functions = dict()
        
        Scope.__init__(self, parent)

    def add_func(self, name, return_type, access_modifier:AccessModifier):
        func = Func(self, name, return_type)
        self.__functions.update({name, func})

    def contains_func(self, name):
        return name in self.__functions
    
    def find_func(self, name):
        if name in self.__functions:
            return self.__functions[name]
        else:
            return None
