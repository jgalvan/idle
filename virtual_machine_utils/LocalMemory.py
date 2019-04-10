from .Memory import Memory
from scopes.CompilationMemory import CompilationMemory

class LocalMemory(Memory):
    def __init__(self, instruction_counter: int):
        super().__init__()
        self.__temporal_memory = Memory()
        self.__instruction_counter = instruction_counter
    
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
    
    def next_instruction(self):
        self.__instruction_counter += 1
        return self.__instruction_counter - 1
    
    def goto(self, counter):
        self.__instruction_counter = counter

    def __str__(self):
        return super().__str__() + " InstrCounter: " + str(self.__instruction_counter)
    