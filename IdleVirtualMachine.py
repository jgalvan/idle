from utils.OperationCode import OperationCode
from virtual_machine_utils.ClassMemory import ClassMemory
from virtual_machine_utils.Memory import Memory
from utils.Stack import Stack

class IdleVirtualMachine():
    def __init__(self, const_quadruples, quadruples):
        self.__const_quadruples = const_quadruples
        self.__quadruples = quadruples
        self.__memory_stack = Stack()
        
        curr_mem = ClassMemory()
        curr_mem.era_func()
        self.__memory_stack.push(curr_mem)

    def run(self):
        self.init_consts()
        # RUN

        for quad in self.__quadruples:
            if OperationCode(quad[0]) == OperationCode.ASSIGN:
                value = self.__memory_stack.peek().get_value(quad[1])
                self.__memory_stack.peek().set_value(value, quad[3])
            elif OperationCode(quad[0]) == OperationCode.ERA:
                self.__memory_stack.peek().era_func()
        

        print(self.__memory_stack.peek())

    def init_consts(self):
        temp = Memory()

        for quad in self.__const_quadruples:
            temp.set_value(quad[1], quad[3])