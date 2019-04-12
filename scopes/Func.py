from .Scope import Scope, AccessModifier

class Func(Scope):
    """Represents a function in the language.
    
    Apart from the inherited scope attributes, it contains a return type and an optional access modifier.
    Access modifiers are not currently fully supported.
    """

    def __init__(self, name, access_modifier:AccessModifier=AccessModifier.PUBLIC):
        self.__return_type = None
        self.__access_modifier = access_modifier
        self.__arguments = []
        self.__func_start = -1
        Scope.__init__(self, name)
    
    @property
    def return_type(self):
        return self.__return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets return_type and prevents from being set more than once."""

        if self.__return_type == None:
            self.__return_type = return_type
        else:
            print("Internal error: Return type already set for %s" % return_type)

    @property
    def arguments(self):
        return self.__arguments

    @property
    def func_start(self):
        return self.__func_start

    @property
    def access_modifier(self):
        return self.__access_modifier
    
    def add_arg(self, arg_name):
        self.__arguments.append(self.find_var(arg_name))

    def change_param_to_ref(self, arg_name):
        var = self.find_var(arg_name)
        var.make_reference()

    def set_func_start(self, start):
        self.__func_start = start