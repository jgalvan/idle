from .IdleEnums import AccessModifier

class Variable():
    def __init__(self, name, var_type, access_modifier:AccessModifier=AccessModifier.public):
        self.__name = name
        self.__var_type = var_type
        self.__access_modifier = access_modifier

    @property
    def name(self):
        return self.__name

    @property
    def var_type(self):
        return self.__var_type

    @property
    def access_modifier(self):
        return self.__access_modifier