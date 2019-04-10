from scopes.CompilationMemory import CompilationMemory
from utils.DataType import DataType
from utils.Stack import Stack

class Memory():
    CONSTANTS = []

    def __init__(self):
        self.__values = {
            DataType.INT: [],
            DataType.FLOAT: [],
            DataType.BOOL: [],
            DataType.STRING: [],
            'Other': []
        }

        self.__defaults = {
            DataType.INT: 0,
            DataType.FLOAT: 0.0,
            DataType.BOOL: False,
            DataType.STRING: "",
            'Other': None
        }
    
    def get_internal_address(self, address):
        return address//100 - 1
    
    def get_value_store(self, address):
        if address % 10 == 1:
            return Memory.CONSTANTS
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        return self.__values[var_type]

    def set_value(self, value, address):
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)

        value_store[internal_address] = value

    def get_value(self, address):
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)

        if value_store[internal_address] == None:
            if var_type == 'Other':
                value_store[internal_address] = ClassMemory()
            else:
                value_store[internal_address] = self.__defaults[var_type]

        return value_store[internal_address]

    def __str__(self):
        return (str(self.__values))


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


class ClassMemory(Memory):
    def __init__(self):
        super().__init__()
        self.__func_memory_stack = Stack()
        self.__next_func = Stack()

    def set_value(self, value, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            super().set_value(value, address)
        else:
            self.__func_memory_stack.peek().set_value(value, address)

    def get_value(self, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            return super().get_value(address)
        else:
            return self.__func_memory_stack.peek().get_value(address)

    def era_func(self, func_start):
        self.__next_func.push(LocalMemory(func_start))
    
    def goto_next_func(self):
        self.__func_memory_stack.push(self.__next_func.pop())

    def end_func(self):
        self.__func_memory_stack.pop()

    def next_instruction(self):
        if self.__func_memory_stack.peek() != None:
            return self.__func_memory_stack.peek().next_instruction()

        return None
    
    def goto(self, counter):
        self.__func_memory_stack.peek().goto(counter)
        
    def __str__(self):
        representation = "----------------------\n"
        representation += "CLASS MEMORY:\n"
        representation += super().__str__() + "\n"

        representation += "\nFUNCTION MEMORY:\n"
        for fnc in self.__func_memory_stack.items:
            representation += fnc.__str__() + "\n"

        representation += "\nNEXT FUNCTIONS:\n"
        for fnc in self.__next_func.items:
            representation += fnc.__str__() + "\n"

        representation += "CONSTANTS:\n"
        representation += self.CONSTANTS.__str__() + "\n"

        representation += "----------------------\n"
        
        return representation