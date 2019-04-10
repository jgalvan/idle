from scopes.CompilationMemory import CompilationMemory
from utils.DataType import DataType

class Memory():
    CONSTANTS = []

    def __init__(self):
        self.__values = {
            DataType.INT: [],
            DataType.FLOAT: [],
            DataType.BOOL: [],
            DataType.STRING: [],
            'Obj': []
        }

        self.__defaults = {
            DataType.INT: 0,
            DataType.FLOAT: 0.0,
            DataType.BOOL: False,
            DataType.STRING: ""
        }
    
    def get_internal_address(self, address):
        return address//100 - 1
    
    def get_value_store(self, address):
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        return self.__values[var_type]

    def set_value(self, value, address):
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address > len(value_store):
            value_store.append(None)

        value_store.append(value)

    def get_value(self, address):
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)

        if value_store[internal_address] == None:
            value_store[internal_address] = self.__defaults[var_type]

        return value_store[internal_address]
