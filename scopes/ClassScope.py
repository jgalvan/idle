from .Scope import Scope, AccessModifier
from .Func import Func

class ClassScope(Scope):
    def __init__(self, name):
        self.__functions = dict()
        self.__current_function = None
        
        Scope.__init__(self, name)

    def add_func(self, name):
        func = Func(self, name)
        self.__current_function = func
        self.__functions.update({name: func})
    
    def update_func_return_type(self, type_name):
        self.__current_function = type_name

    def contains_func(self, name):
        return name in self.__functions
    
    def find_func(self, name):
        if name in self.__functions:
            return self.__functions[name]
        else:
            return None
