from utils.OperationCode import OperationCode
from virtual_machine_utils.Memory import Memory, ClassMemory
from utils.Stack import Stack

class IdleVirtualMachine():
    def __init__(self, const_quadruples, quadruples):
        self.__const_quadruples = const_quadruples
        self.__quadruples = quadruples
        self.__memory_stack = Stack()
        self.__next_class_stack = Stack()

        curr_class = ClassMemory()
        curr_class.era_func(self.__quadruples[0][3])
        curr_class.goto_next_func()
        self.__memory_stack.push(curr_class)

    @property
    def current_memory(self):
        return self.__memory_stack.peek()

    def run(self):
        self.init_consts()
        # RUN

        next_quad = self.next_instruction()
        while next_quad != None:
            if OperationCode(next_quad[0]) == OperationCode.GOTO:
                self.current_memory.goto(next_quad[3])
            elif OperationCode(next_quad[0]) == OperationCode.ASSIGN:
                value = self.current_memory.get_value(next_quad[1])
                self.current_memory.set_value(value, next_quad[3])
            elif OperationCode(next_quad[0]) == OperationCode.ERA:
                if next_quad[2] != None:
                    obj = self.current_memory.get_value(next_quad[2])
                    obj.era_func(next_quad[1])
                    self.__next_class_stack.push(obj)
                else:
                    self.current_memory.era_func(next_quad[1])
            elif OperationCode(next_quad[0]) == OperationCode.GOSUB:
                if not self.__next_class_stack.isEmpty():
                    self.__memory_stack.push(self.__next_class_stack.pop())
                self.current_memory.goto_next_func()
            elif OperationCode(next_quad[0]) == OperationCode.ENDPROC:
                self.current_memory.end_func()

            print("===== EXECUTED: " + str(next_quad) + " =========")
            print(self.current_memory)
            
            next_quad = self.next_instruction()

    def next_instruction(self):
        counter = self.current_memory.next_instruction()
        if counter != None:
            return self.__quadruples[counter]
        elif self.__memory_stack.size() > 1:
            self.__memory_stack.pop()
            return self.next_instruction()

        return None

    def init_consts(self):
        temp = Memory()

        for quad in self.__const_quadruples:
            temp.set_value(quad[1], quad[3])