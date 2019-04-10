from utils.Stack import Stack
from scopes.CompilationMemory import CompilationMemory
from .Memory import Memory

class ClassMemory(Memory):
    def __init__(self):
        super().__init__()
        self.__func_memory_stack = Stack()

    def era_func(self):
        self.__func_memory_stack.push(Memory())
    
    def end_func(self):
        self.__func_memory_stack.pop()

    def set_value(self, value, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            super().set_value(value, address)
        else:
            self.__func_memory_stack.peek().set_value(value, address)

    def get_value(self, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            return super().get_value(address)
        elif address % 10 == CompilationMemory.CONSTANT_ID:
            return super().get_value(address)
        else:
            return self.__func_memory_stack.peek().get_value(address)
        
    def __str__(self):
        representation = "----------------------\n"
        representation += "CLASS MEMORY:\n"
        representation += super().__str__()
        representation += "\nFUNCTION MEMORY:\n"
        
        for fnc in self.__func_memory_stack.items:
            representation += fnc.__str__() + "\n"

        representation += "\nCONSTANTS:\n"
        representation += self.CONSTANTS.__str__() + "\n"

        representation += "----------------------\n"
        
        return representation