from .Scope import Scope, AccessModifier

class Func(Scope):
    def __init__(self, parent: Scope, name, return_type, access_modifier:AccessModifier=AccessModifier.public):
        self.__name = name
        self.__return_type = return_type
        self.__access_modifier = access_modifier

        Scope.__init__(self, parent)
