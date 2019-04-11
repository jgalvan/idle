from utils.OperationCode import OperationCode
from virtual_machine_utils.Memory import Memory, ClassMemory
from utils.Stack import Stack

class IdleVirtualMachine():
    def __init__(self, const_quadruples, quadruples, debug = False):
        self.__const_quadruples = const_quadruples
        self.__quadruples = quadruples
        self.__memory_stack = Stack()
        self.__next_class_stack = Stack()
        self.__debug = debug

        curr_class = ClassMemory()
        curr_class.era_func(self.__quadruples[0][3])
        curr_class.goto_next_func()
        self.__memory_stack.push(curr_class)

    @property
    def current_memory(self):
        return self.__memory_stack.peek()

    def run(self):
        instruction_set = {
            OperationCode.GOTO: self.run_goto,
            OperationCode.GOTOF: self.run_gotof,
            OperationCode.GOTOT: self.run_gotot,
            OperationCode.ASSIGN: self.run_assign,
            OperationCode.ERA: self.run_era,
            OperationCode.PARAM: self.run_param,
            OperationCode.GOSUB: self.run_gosub,
            OperationCode.RETURN: self.run_return,
            OperationCode.ENDPROC: self.run_endproc,
            OperationCode.ADD: self.run_add,
            OperationCode.SUB: self.run_sub,
            OperationCode.MULT: self.run_mult,
            OperationCode.DIV: self.run_div,
            OperationCode.GT: self.run_gt,
            OperationCode.LT: self.run_lt,
            OperationCode.GE: self.run_ge,
            OperationCode.LE: self.run_le,
            OperationCode.EQUAL: self.run_equal,
            OperationCode.NOTEQUAL: self.run_not_equal,
            OperationCode.PRINT: self.run_print
        }

        self.init_consts()

        next_quad = self.next_instruction()
        while next_quad != None:
            instruction = instruction_set[OperationCode(next_quad[0])]
            instruction(next_quad)

            if self.__debug:
                print("===== EXECUTED: " + str(next_quad) + " =========")
                print(self.current_memory)
            
            next_quad = self.next_instruction()

    def init_consts(self):
        temp = Memory()

        for quad in self.__const_quadruples:
            temp.set_value(quad[1], quad[3])

    def next_instruction(self):
        counter = self.current_memory.next_instruction()
        if counter != None:
            return self.__quadruples[counter]
        elif self.__memory_stack.size() > 1:
            self.__memory_stack.pop()
            return self.next_instruction()

        return None
    
    # INSTRUCTION SET FUNCTIONS

    def run_goto(self, quad):
        self.current_memory.goto(quad[3])
    
    def run_gotof(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        if not op1:
            self.current_memory.goto(quad[3])

    def run_gotot(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        if op1:
            self.current_memory.goto(quad[3])

    def run_assign(self, quad):
        value = self.current_memory.get_value(quad[1])
        self.current_memory.set_value(value, quad[3])

    def run_era(self, quad):
        if quad[2] != None:
            obj = self.current_memory.get_value(quad[2])
            obj.era_func(quad[1])
            self.__next_class_stack.push(obj)
        else:
            self.current_memory.era_func(quad[1])

    def run_param(self, quad):
        value = self.current_memory.get_value(quad[1])

        if not self.__next_class_stack.isEmpty():
            self.__next_class_stack.peek().send_param(value, quad[3])
        else:
            self.current_memory.send_param(value, quad[3])
    
    def run_gosub(self, quad):
        if not self.__next_class_stack.isEmpty():
            self.__memory_stack.push(self.__next_class_stack.pop())
        self.current_memory.goto_next_func()

    def run_return(self, quad):
        value = self.current_memory.get_value(quad[1])

        # If there is another function in stack, it means it will return to that function within class
        if self.current_memory.can_return():
            counter = self.current_memory.prev_func_last_instruction()
            address = self.__quadruples[counter][3]
            self.current_memory.return_value(value, address)
        else: # Return of object function call
            prev_class = self.__memory_stack.peek_next_to_last()
            counter = prev_class.curr_func_last_instruction()
            address = self.__quadruples[counter][3]
            prev_class.set_value(value, address)

        self.run_endproc()
    
    def run_endproc(self, quad=None):
        self.current_memory.end_func()

    def run_add(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 + op2, quad[3])

    def run_sub(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 - op2, quad[3])

    def run_mult(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 * op2, quad[3])

    def run_div(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        if isinstance(op1, int) and isinstance(op2, int):
            self.current_memory.set_value(op1 // op2, quad[3])
        else:
            self.current_memory.set_value(op1 / op2, quad[3])

    def run_gt(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 > op2, quad[3])
    
    def run_lt(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 < op2, quad[3])

    def run_equal(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 == op2, quad[3])

    def run_ge(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 >= op2, quad[3])

    def run_le(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 <= op2, quad[3])

    def run_not_equal(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        op2 = self.current_memory.get_value(quad[2])
        self.current_memory.set_value(op1 != op2, quad[3])

    def run_print(self, quad):
        op1 = self.current_memory.get_value(quad[1])
        if isinstance(op1, bool):
            op1 = str(op1).lower()
        print(op1)
        