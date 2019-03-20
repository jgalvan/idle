from .Variable import *

class Scope():
    """Represents a scope in the language.

    It contains its own set of variables and it may be nested in another scope,
    which is represented via the parent. 
    
    Name attribute is optional.
    """

    def __init__(self, name=None, parent: "Scope"=None):
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
        """Adds a variable to be commited. Assummes variable does not exist.
        
        To fully save a variable into the function's symbol table, you must
        call commit_vars with the type.
        """
        self.__pending_variables.append(var_name)
    
    def commit_vars(self, type_name):
        """Saves pending variables with type 'type_name'.
        
        Expected to be called after variable type is parsed. Assummes variable
        doesn't already exist.
        """

        for var_name in self.__pending_variables:
            current_var = Variable(var_name, type_name)
            self.__variables[var_name] = current_var
        
        self.__pending_variables.clear()
    
    def contains_var(self, name) -> bool:
        """Checks if variable has been declared specifically in current scope."""

        return name in self.__variables
    
    def var_in_scope(self, name) -> bool:
        """Checks if variable is available in scope.
        
        Variable may have been declared in scope or any of the parents.
        """
        
        return self.find_var(name) != None

    def find_var(self, name) -> Variable:
        """Looks for variable in scope or parents and returns None if not found."""
        if name in self.__variables:
            return self.__variables[name]
        elif self.__parent:
            return self.__parent.find_var(name)
        else:
            return None