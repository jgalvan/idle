from .Scope import Scope, AccessModifier

class Func(Scope):
    def __init__(self, parent: Scope, name, access_modifier:AccessModifier=AccessModifier.public):
        self.__return_type = None
        self.__access_modifier = access_modifier

        Scope.__init__(self, name, parent)
    
    @property
    def return_type(self):
        return self.__return_type

    @return_type.setter
    def return_type(self, return_type):
        if self.__return_type == None:
            return_type = return_type
        else:
            Exception("Internal error: Return type already set for %s" % return_type)