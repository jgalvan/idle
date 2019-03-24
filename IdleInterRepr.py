from utils.Stack import Stack
from utils.SemanticCube import SemanticCube
from utils.DataType import DataType
from scopes.Variable import Variable

class Temporal:
    TEMP_PREFIX = "__temp__"

    def __init__(self):
        self.__count = 0
        self.__available = []

    def next(self, var_type):
        if self.__available.count > 0:
            next_var = self.__available.pop()
            next_var.change_type(var_type)
            return next_var

        next_var_name = self.TEMP_PREFIX + self.__count
        next_var = Variable(next_var_name, var_type)
        self.__count = self.__count + 1
        return next_var

    @staticmethod
    def is_temp(var):
        return var.name.starts_with(Temporal.TEMP_PREFIX)  

    def free_up(self, var):
        self.__available.append(var)

class IdleInterRepr:
    def __init__(self):
        self.__temporals = Temporal()
        self.__operands_stack = Stack()
        self.__operators_stack = Stack()
        self.__quads = []
    
    def add_var(self, var):
        self.__operands_stack.push(var)
    
    def add_operator(self, operator):
        self.__operators_stack.push(operator)

    def __resolve_oper(self) -> bool:
        right_oper = self.__operands_stack.pop()
        left_oper = self.__operands_stack.pop()
        operator = self.__operands_stack.pop()

        result_type = SemanticCube.check(left_oper.var_type, right_oper.var_type, operator)

        if result_type == DataType.ERROR:
            return False

        result = self.__temporals.next(result_type)
        self.__quads.append((operator, left_oper, right_oper, result))

        if Temporal.is_temp(left_oper):
            self.__temporals.free_up(left_oper)
        
        if Temporal.is_temp(right_oper):
            self.__temporals.free_up(right_oper)

        return True

    def check_addsub(self) -> bool:
        if self.__operators_stack.peek == '+' or self.__operators_stack.peek == '-':
            return self.__resolve_oper
    
    def check_divmult(self) -> bool:
        if self.__operators_stack.peek == '*' or self.__operators_stack.peek == '/':
            return self.__resolve_oper