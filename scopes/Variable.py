from .IdleEnums import AccessModifier
from utils.DataType import DataType

class ArrayInfo():
    def __init__(self, var_type, size):
        self.var_type = var_type
        self.size = size

class Variable():
    """Represents a variable in language. It has a name, type and access modifier.
    
    Access modifiers are not currently fully supported.
    """

    def __init__(self, name, var_type, address):
        self.__name = name
        self.__var_type = var_type
        self.__address = address

        self.__is_param_by_ref = False
        self.__array_info = None
        self.__pointer_type = None

    @property
    def name(self):
        return self.__name

    @property
    def var_type(self):
        if self.__var_type == DataType.POINTER:
            return self.__pointer_type
        
        return self.__var_type

    @property
    def access_modifier(self):
        return AccessModifier.get_access_modifier(self.__name)

    @property
    def address(self):
        return self.__address
    
    @property
    def is_param_by_ref(self):
        return self.__is_param_by_ref

    @property
    def array_type(self):
        return self.__array_info.var_type
    
    @property
    def array_size(self):
        return self.__array_info.size

    def change_type(self, var_type):
        self.__var_type = var_type

    def make_array(self, size):
        self.__array_info = ArrayInfo(self.__var_type, size)
        self.__var_type = DataType.ARRAY

    def make_reference(self):
        self.__is_param_by_ref = True

    def make_pointer(self, var_type: DataType):
        self.__pointer_type = var_type

    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.__name, self.__var_type, self.__address, self.__access_modifier)