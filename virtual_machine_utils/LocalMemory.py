from .Memory import Memory
from scopes.CompilationMemory import CompilationMemory

class LocalMemory(Memory):
    def __init__(self):
        super().__init__()
        self.__temporal_memory = Memory()
    
    def set_value(self, value, address):
        if address % 10 == CompilationMemory.TEMP_ID:
            self.__temporal_memory.set_value(value, address)
        else:
            super().set_value(value, address)

    def get_value(self, address):
        if address % 10 == CompilationMemory.TEMP_ID:
            return self.__temporal_memory.get_value(address)
        else:
            return super().get_value(address)

    