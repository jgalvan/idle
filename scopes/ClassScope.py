from .Scope import Scope, AccessModifier
from .Func import Func
from .CompilationMemory import CompilationMemory
import copy

# Represents a 
class ClassScope(Scope):
    """Represents a class in the language. 
    
    Apart from the inherited scope attributes, it contains a group of functions.
    """

    def __init__(self, name, parent_class = None):
        self.__functions = dict()
        self.__current_function = None
        self.__parent_class = parent_class
        
        Scope.__init__(self, name)

        if self.__parent_class != None:
            self.compilation_memory = copy.deepcopy(self.__parent_class.compilation_memory)

        self.compilation_memory.scope_type = CompilationMemory.INSTANCE_ID

    @property
    def parent_class(self):
        return self.__parent_class

    def add_func(self, name, access_modifier: AccessModifier):
        """Adds a function to the class. Assumes function does not exist."""

        func = Func(name, access_modifier)
        self.__current_function = func
        self.__functions.update({name: func})
    
    def update_func_return_type(self, type_name):
        """Changes return type of last function added. 
        
        Expected to be called after function return type is parsed.
        """

        self.__current_function = type_name

    def contains_func(self, name) -> bool:
        """Checks existence of function in class, not parent classes."""

        return name in self.__functions
    
    def find_func(self, name) -> Func:
        """Looks for function in class and returns None if not found."""

        if name in self.__functions:
            return self.__functions[name]
        elif self.__parent_class:
            return self.__parent_class.find_func(name)
        else:
            return None

    def find_instance_var(self, name):
        """Looks for variable in class or parents and returns None if not found."""
        
        if name in self.variables:
            return self.variables[name]
        elif self.__parent_class:
            return self.__parent_class.find_instance_var(name)
        else:
            return None
