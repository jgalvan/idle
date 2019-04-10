from utils.Stack import Stack
from scopes.CompilationMemory import CompilationMemory
from .Memory import Memory

class ClassMemory(Memory):
    def __init__(self):
        Memory.__init__(self)
        self.__func_memory_stack = Stack()

    def era_func(self):
        self.__func_memory_stack.push(Memory())
    
    def end_func(self):
        self.__func_memory_stack.pop()

    def set_value(self, value, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            Memory.set_value(self, value, address)
        else:
            self.__func_memory_stack.peek().set_value(self, value, address)

    def get_value(self, address):
        if address % 10 == CompilationMemory.INSTANCE_ID:
            Memory.get_value(self, address)
        else:
            self.__func_memory_stack.peek().get_value(self, address)