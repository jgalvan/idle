from scopes.CompilationMemory import CompilationMemory
from utils.DataType import DataType
from utils.Stack import Stack
import copy

class VarWrapper():
    def __init__(self, value):
        self.value = value

class Memory():
    CONSTANTS = {
        DataType.INT: [],
        DataType.FLOAT: [],
        DataType.BOOL: [],
        DataType.STRING: [],
    }

    def __init__(self):
        self.__values = {
            DataType.INT: [],
            DataType.FLOAT: [],
            DataType.BOOL: [],
            DataType.STRING: [],
            'Other': [],
            DataType.POINTER: []
        }

        self.__defaults = {
            DataType.INT: 0,
            DataType.FLOAT: 0.0,
            DataType.BOOL: False,
            DataType.STRING: "",
            'Other': None,
            DataType.POINTER: 0
        }
    
    def get_type(self, address):
        return CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]

    def get_internal_address(self, address):
        return address//100 - 1
    
    def get_value_store(self, address):
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        if address % 10 == 1:
            return Memory.CONSTANTS[var_type]
        return self.__values[var_type]

    def get_reference(self, address):
        var_type = CompilationMemory.VAR_TYPE_FROM_CODE[(address%100)//10]
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)

        if value_store[internal_address] == None:
            if var_type == 'Other':
                value_store[internal_address] = VarWrapper(ClassMemory())
            else:
                value_store[internal_address] = VarWrapper(self.__defaults[var_type])

        return value_store[internal_address]
    
    def get_value(self, address):
        return self.get_reference(address).value

    def set_reference(self, reference, address):
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)
        
        value_store[internal_address] = reference

    def set_value(self, value, address):
        internal_address = self.get_internal_address(address)
        value_store = self.get_value_store(address)

        while internal_address >= len(value_store):
            value_store.append(None)
        
        if value_store[internal_address] == None:
            value_store[internal_address] = VarWrapper(copy.deepcopy(value))
        else:
            value_store[internal_address].value = copy.deepcopy(value)

    def __str__(self):
        return (str(self.__values))


class LocalMemory(Memory):
    def __init__(self, instruction_counter: int):
        super().__init__()
        self.__temporal_memory = Memory()
        self.__instruction_counter = instruction_counter
    
    @property
    def last_instruction(self):
        return self.__instruction_counter - 1

    def set_reference(self, reference, address):
        if address % 10 == CompilationMemory.TEMP_ID:
            self.__temporal_memory.set_reference(reference, address)
        else:
            super().set_reference(reference, address)

    def get_reference(self, address):
        if address % 10 == CompilationMemory.TEMP_ID:
            return self.__temporal_memory.get_reference(address)
        else:
            return super().get_reference(address)

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

    def set_reference(self, reference, address):
        if self.get_type(address) == DataType.POINTER:
            actual_address = self.__func_memory_stack.peek().get_value(address)
            self.set_reference(reference, actual_address)
        elif address % 10 == CompilationMemory.INSTANCE_ID:
            super().set_reference(reference, address)
        else:
            self.__func_memory_stack.peek().set_reference(reference, address)

    def get_reference(self, address):
        if self.get_type(address) == DataType.POINTER:
            actual_address = self.__func_memory_stack.peek().get_value(address)
            return self.get_reference(actual_address)
        elif address % 10 == CompilationMemory.INSTANCE_ID:
            return super().get_reference(address)
        else:
            return self.__func_memory_stack.peek().get_reference(address)

    def set_value(self, value, address):
        if self.get_type(address) == DataType.POINTER:
            actual_address = self.__func_memory_stack.peek().get_value(address)
            self.set_value(value, actual_address)
        elif address % 10 == CompilationMemory.INSTANCE_ID:
            super().set_value(value, address)
        else:
            self.__func_memory_stack.peek().set_value(value, address)

    def get_value(self, address):
        if self.get_type(address) == DataType.POINTER:
            actual_address = self.__func_memory_stack.peek().get_value(address)
            return self.get_value(actual_address)
        if address % 10 == CompilationMemory.INSTANCE_ID:
            return super().get_value(address)
        else:
            return self.__func_memory_stack.peek().get_value(address)

    def set_pointer_address(self, pointer_address, pointing_address):
        self.__func_memory_stack.peek().set_value(pointing_address, pointer_address)

    def era_func(self, func_start):
        self.__next_func.push(LocalMemory(func_start))

    def send_param(self, value, address):
        self.__next_func.peek().set_value(value, address)
    
    def send_param_by_ref(self, reference, address):
        self.__next_func.peek().set_reference(reference, address)

    def can_return(self):
        return self.__func_memory_stack.size() > 1

    def curr_func_last_instruction(self):
        return self.__func_memory_stack.peek().last_instruction

    def prev_func_last_instruction(self):
        return self.__func_memory_stack.peek_next_to_last().last_instruction

    def return_value(self, value, address):
        self.__func_memory_stack.peek_next_to_last().set_value(value, address)
    
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