from .Scope import Scope, AccessModifier

class Func(Scope):
    """Represents a function in the language.
    
    Apart from the inherited scope attributes, it contains a return type and an optional access modifier.
    Access modifiers are not currently fully supported.
    """

    def __init__(self, parent: Scope, name, access_modifier:AccessModifier=AccessModifier.public):
        self.__return_type = None
        self.__access_modifier = access_modifier
        self.__arguments = []
        Scope.__init__(self, name, parent)
    
    @property
    def return_type(self):
        return self.__return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets return_type and prevents from being set more than once."""

        if self.__return_type == None:
            return_type = return_type
        else:
            print("Internal error: Return type already set for %s" % return_type)
    
    def add_arg(self, arg_name):
        self.__arguments.append(self.find_var(arg_name))
        print("added argument ", arg_name)