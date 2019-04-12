from .IdleEnums import AccessModifier

class Variable():
    """Represents a variable in language. It has a name, type and access modifier.
    
    Access modifiers are not currently fully supported.
    """

    def __init__(self, name, var_type, address, access_modifier:AccessModifier=AccessModifier.PUBLIC):
        self.__name = name
        self.__var_type = var_type
        self.__address = address
        self.__access_modifier = access_modifier

        self.__is_param_by_ref = False

    @property
    def name(self):
        return self.__name

    @property
    def var_type(self):
        return self.__var_type

    @property
    def access_modifier(self):
        return self.__access_modifier

    @property
    def address(self):
        return self.__address
    
    @property
    def is_param_by_ref(self):
        return self.__is_param_by_ref

    def change_type(self, var_type):
        self.__var_type = var_type

    def make_reference(self):
        self.__is_param_by_ref = True

    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.__name, self.__var_type, self.__address, self.__access_modifier)