from utils.Stack import Stack
from scopes.CompilationMemory import CompilationMemory
from .LocalMemory import LocalMemory
from .Memory import Memory

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