from utils.OperationCode import OperationCode
from virtual_machine_utils.ClassMemory import ClassMemory
from virtual_machine_utils.Memory import Memory
from utils.Stack import Stack

class IdleVirtualMachine():
    def __init__(self, const_quadruples, quadruples):
        self.__const_quadruples = const_quadruples
        self.__quadruples = quadruples
        self.__memory_stack = Stack()

        curr_class = ClassMemory()
        curr_class.era_func(self.__quadruples[0][3])
        curr_class.goto_next_func()
        self.__memory_stack.push(curr_class)

    def run(self):
        self.init_consts()
        # RUN

        next_quad = self.next_instruction()
        while next_quad != None:
            if OperationCode(next_quad[0]) == OperationCode.GOTO:
                self.__memory_stack.peek().goto(next_quad[3])
            elif OperationCode(next_quad[0]) == OperationCode.ASSIGN:
                value = self.__memory_stack.peek().get_value(next_quad[1])
                self.__memory_stack.peek().set_value(value, next_quad[3])
            elif OperationCode(next_quad[0]) == OperationCode.ERA:
                self.__memory_stack.peek().era_func(next_quad[1])
            elif OperationCode(next_quad[0]) == OperationCode.GOSUB:
                self.__memory_stack.peek().goto_next_func()
            elif OperationCode(next_quad[0]) == OperationCode.ENDPROC:
                self.__memory_stack.peek().end_func()

            print("===== EXECUTED: " + str(next_quad) + " =========")
            print(self.__memory_stack.peek())
            
            next_quad = self.next_instruction()

    def next_instruction(self):
        counter = self.__memory_stack.peek().next_instruction()
        if counter != None:
            return self.__quadruples[counter]
        
        return None

    def init_consts(self):
        temp = Memory()

        for quad in self.__const_quadruples:
            temp.set_value(quad[1], quad[3])