from utils.Stack import Stack
from utils.SemanticCube import SemanticCube
from utils.DataType import DataType
from utils.OperationCode import OperationCode
from scopes.Variable import Variable

class Temporal:
    TEMP_PREFIX = "__temp__"

    def __init__(self):
        self.__count = 0
        self.__available = []

    def next(self, var_type):
        if len(self.__available) > 0:
            next_var = self.__available.pop()
            next_var.change_type(var_type)
            return next_var

        next_var_name = self.TEMP_PREFIX + str(self.__count)
        next_var = Variable(next_var_name, var_type)
        self.__count = self.__count + 1
        return next_var

    @staticmethod
    def is_temp(var):
        return var.name.startswith(Temporal.TEMP_PREFIX)  

    def free_up(self, var):
        self.__available.append(var)

class IdleInterRepr:
    def __init__(self):
        self.__temporals = Temporal()
        self.__operands_stack = Stack()
        self.__operators_stack = Stack()
        self.__quads = []
        self.__jump_stack = Stack()

    @property
    def quads(self):
        return self.__quads
    
    def add_var(self, var):
        self.__operands_stack.push(var)
    
    def add_operator(self, operator):
        self.__operators_stack.push(OperationCode(operator))

    def __resolve_oper(self) -> bool:
        right_oper = self.__operands_stack.pop()
        left_oper = self.__operands_stack.pop()
        operator = self.__operators_stack.pop()

        result_type = SemanticCube.check(operator, left_oper.var_type, right_oper.var_type)

        if result_type == DataType.ERROR:
            return False

        result = self.__temporals.next(result_type)
        self.__quads.append((operator.to_code(), left_oper.name, right_oper.name, result.name))
        self.__operands_stack.push(result)

        if Temporal.is_temp(left_oper):
            self.__temporals.free_up(left_oper)
        
        if Temporal.is_temp(right_oper):
            self.__temporals.free_up(right_oper)

        return True

    def check_addsub(self) -> bool:
        if OperationCode.is_add_sub(self.__operators_stack.peek()):
            return self.__resolve_oper()
        
        return True
    
    def check_divmult(self) -> bool:
        if OperationCode.is_div_mult(self.__operators_stack.peek()):
            return self.__resolve_oper()

        return True

    def check_relop(self) -> bool:
        if OperationCode.is_relop(self.__operators_stack.peek()):
            return self.__resolve_oper()

        return True

    def open_parenthesis(self):
        self.__operators_stack.push(OperationCode.FAKEBOTTOM)
    
    def close_parenthesis(self):
        self.__operators_stack.pop()

    def assign(self, var) -> bool:
        oper = self.__operands_stack.pop()

        if oper.var_type != var.var_type:
            return False

        self.__quads.append((OperationCode.ASSIGN.to_code(), oper.name, None, var.name))
        return True

    def read(self, read_type):
        result = self.__temporals.next(read_type)

        if read_type == DataType.INT:
            self.__quads.append((OperationCode.READINT.to_code(), None, None, result.name))

        if read_type == DataType.FLOAT:
            self.__quads.append((OperationCode.READFLOAT.to_code(), None, None, result.name))
        
        if read_type == DataType.STRING:
            self.__quads.append((OperationCode.READSTRING.to_code(), None, None, result.name))
        
        self.__operands_stack.push(result)

    def print_st(self):
        oper = self.__operands_stack.pop()
        self.__quads.append((OperationCode.PRINT.to_code(), oper.name, None, None))

    def start_while(self):
        self.__jump_stack.push(len(self.__quads))
    
    def end_while_expr(self) -> bool:
        expr_result = self.__operands_stack.pop()

        if expr_result.var_type != DataType.BOOL:
            return False

        self.__quads.append((OperationCode.GOTOF.to_code(), expr_result.name, None, None))
        self.__jump_stack.push(len(self.__quads)-1)

        return True
    
    def end_while(self):
        expr_end = self.__jump_stack.pop()
        while_start = self.__jump_stack.pop()

        # Add GOTO to loop back to while start
        self.__quads.append((OperationCode.GOTO.to_code(), None, None, while_start))

        # Update GOTOF jump address after expression
        expr_end_quad = list(self.__quads[expr_end])
        expr_end_quad[3] = len(self.__quads)
        self.__quads[expr_end] = tuple(expr_end_quad)

    def start_for_assign(self):
        # Save current quad list into temporal space and reset quads
        self.__temp_quads = self.__quads
        self.__quads = []
    
    def end_for_assign(self):
        # Switch quad list with the temporal quads generated from the for assignment
        quads = self.__temp_quads
        self.__temp_quads = self.__quads
        self.__quads = quads
    
    def end_for_block(self):
        # Add temporal quads from assignment to end of block
        self.__quads.extend(self.__temp_quads)

    def end_if_expr(self) -> bool:
        expr_result = self.__operands_stack.pop()

        if expr_result.var_type != DataType.BOOL:
            return False

        self.__quads.append(('GOTOF', expr_result.name, None, None))
        false_jumps = Stack()
        false_jumps.push(len(self.__quads)-1)
        self.__jump_stack.push(false_jumps)

        return True

    def fill_if_end_jumps(self):
        fill_jumps = self.__jump_stack.pop()
        while not fill_jumps.isEmpty():
            expr_end = fill_jumps.pop()
            # Update GOTOF jump address after expression
            expr_end_quad = list(self.__quads[expr_end])
            expr_end_quad[3] = len(self.__quads)
            self.__quads[expr_end] = tuple(expr_end_quad)

    def start_else_ifs(self):
        goto_end_jumps = Stack()
        goto_false_jumps = self.__jump_stack.pop()
        self.__jump_stack.push(goto_end_jumps)
        self.__jump_stack.push(goto_false_jumps)

    def add_else(self):
        self.__quads.append(('GOTO', None, None, None))
        false_jumps = self.__jump_stack.pop()
        false_jump = false_jumps.pop()

        # Add quad to stack of quads that should jump to the end of if
        goto_end_jumps = self.__jump_stack.pop()
        goto_end_jumps.push(len(self.__quads)-1)
        self.__jump_stack.push(goto_end_jumps)

        # Update GOTOF jump address from previous if / else if
        expr_false_jump = list(self.__quads[false_jump])
        expr_false_jump[3] = len(self.__quads)
        self.__quads[false_jump] = tuple(expr_false_jump)
    
