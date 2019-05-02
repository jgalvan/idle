from utils.Stack import Stack
from utils.SemanticCube import SemanticCube
from utils.DataType import DataType
from utils.OperationCode import OperationCode
from scopes.Variable import Variable
from scopes.Func import Func
from scopes.CompilationMemory import CompilationMemory, Temporal

class IdleInterRepr:
    def __init__(self):
        self.__temporals = Temporal()
        self.__operands_stack = Stack()
        self.__operators_stack = Stack()
        self.__quads = []
        self.__jump_stack = Stack()
        self.__func_calls_stack = Stack()
        self.__param_counter_stack = Stack()

    @property
    def quads(self):
        return self.__quads

    def constant_quads(self):
        const_quads = []

        for const_dict in CompilationMemory.CONSTANTS.values():
            for name,var in const_dict.items():
                const_quads.append((OperationCode.ASSIGN, name, None, var.address))

        return const_quads

    def get_last_var(self):
        """Returns top of operands stack. Expects to be called only when calling function or variable within object."""

        return self.__operands_stack.pop()
    
    def add_goto_main(self):
        self.quads.append((OperationCode.GOTO, None, None, None))

    def set_main(self, main_func: Func):
        start = list(self.__quads[0])
        start[3] = main_func.func_start
        self.__quads[0] = tuple(start)
    
    def add_var(self, var):
        self.__operands_stack.push(var)
    
    def add_access_instance_var(self, class_ref: Variable, obj_var: Variable):

        temp = self.__temporals.next(obj_var.var_type)
        self.__quads.append((OperationCode.ASSIGN, class_ref.address, obj_var.address, temp.address))
        self.__operands_stack.push(temp)
    
    def array_access(self, var):
        index_var = self.__operands_stack.pop()

        if index_var.var_type != DataType.INT:
            return False

        result = self.__temporals.next(DataType.POINTER)
        result.make_pointer(var.array_type)

        self.__quads.append((OperationCode.ARRINDEXCHECK.to_code(), 0, var.array_size-1, index_var.address))
        self.__quads.append((OperationCode.ARRACCESS.to_code(), var.address, index_var.address, result.address))
        self.__operands_stack.push(result)
        self.__temporals.free_up_if_temp(index_var)
        return True

    def array_sort(self, var):
        self.__quads.append((OperationCode.ARRSORT.to_code(), 0, var.array_size, var.address))
    
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
        self.__quads.append((operator.to_code(), left_oper.address, right_oper.address, result.address))
        self.__operands_stack.push(result)

        self.__temporals.free_up_if_temp(left_oper)
        self.__temporals.free_up_if_temp(right_oper)

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

    def assign(self) -> bool:
        oper = self.__operands_stack.pop()
        var = self.__operands_stack.pop()

        if oper.var_type != var.var_type:
            return False
        
        self.__temporals.free_up_if_temp(oper)

        self.__quads.append((OperationCode.ASSIGN.to_code(), oper.address, None, var.address))
        return True

    def short_var_decl_assign(self) -> DataType:
        oper = self.__operands_stack.pop()
        var = self.__operands_stack.pop()
        
        self.__temporals.free_up_if_temp(oper)

        self.__quads.append((OperationCode.ASSIGN.to_code(), oper.address, None, var.address))
        return oper.var_type

    def read(self, read_type):
        result = self.__temporals.next(read_type)

        if read_type == DataType.INT:
            self.__quads.append((OperationCode.READINT.to_code(), None, None, result.address))

        if read_type == DataType.FLOAT:
            self.__quads.append((OperationCode.READFLOAT.to_code(), None, None, result.address))
        
        if read_type == DataType.STRING:
            self.__quads.append((OperationCode.READSTRING.to_code(), None, None, result.address))
        
        self.__operands_stack.push(result)
        temp_func = Func('temp')
        temp_func.return_type = read_type
        self.__func_calls_stack.push(temp_func)

    def to_string(self):
        oper = self.__operands_stack.pop()
        result = self.__temporals.next(DataType.STRING)

        self.__quads.append((OperationCode.TOSTRING.to_code(), oper.address, None, result.address))
        
        self.__operands_stack.push(result)
        temp_func = Func('temp')
        temp_func.return_type = DataType.STRING
        self.__func_calls_stack.push(temp_func)

    def print_st(self):
        oper = self.__operands_stack.pop()
        self.__quads.append((OperationCode.PRINT.to_code(), oper.address, None, None))

    def start_while(self):
        self.__jump_stack.push(len(self.__quads))
    
    def end_while_expr(self) -> bool:
        expr_result = self.__operands_stack.pop()

        if expr_result.var_type != DataType.BOOL:
            return False

        self.__quads.append((OperationCode.GOTOF.to_code(), expr_result.address, None, None))
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

        self.__quads.append((OperationCode.GOTOF.to_code(), expr_result.address, None, None))
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
        self.__quads.append((OperationCode.GOTO.to_code(), None, None, None))
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
    
    def add_func_era(self, func_called: Func, obj_var: Variable = None):
        if obj_var != None:
            # If call belongs to object, add object reference to change instance contexts
            self.__quads.append((OperationCode.ERA, func_called.func_start, obj_var.address, None))
        elif func_called.name == func_called.return_type:
            temp = self.__temporals.next(func_called.return_type)
            self.__quads.append((OperationCode.ERA, func_called.func_start, temp.address, None))
            self.__operands_stack.push(temp)
        elif func_called.name == "__default_constructor__":
            temp = self.__temporals.next(func_called.return_type)
            self.__operands_stack.push(temp)
        else:
            self.__quads.append((OperationCode.ERA, func_called.func_start, None, None))
        
        self.__func_calls_stack.push(func_called)
        self.__param_counter_stack.push(0)
    
    def add_func_param(self):
        func_called = self.__func_calls_stack.peek()
        origin_var = self.__operands_stack.pop()
        param_counter = self.__param_counter_stack.pop()
        self.__param_counter_stack.push(param_counter + 1)

        # More arguments given than requested
        if param_counter >= len(func_called.arguments):
            return (True, None) # Ignore, later will be caught on add_func_gosub
        
        # Check parameter type matching
        destination_var = func_called.arguments[param_counter]
        if origin_var.var_type != destination_var.var_type:
            return (False, destination_var.address, destination_var.var_type)

        if destination_var.is_param_by_ref:
            self.__quads.append((OperationCode.PARAMREF, origin_var.address, None, destination_var.address))
        else:
            self.__quads.append((OperationCode.PARAM, origin_var.address, None, destination_var.address))
        return (True, None)

    def add_func_gosub(self):
        func_called = self.__func_calls_stack.peek()

        if func_called:
            if func_called.name != "__default_constructor__": # Ignore default constructor
                
                # If function has return value, save return in temporal
                if func_called.return_type != None:
                    if func_called.return_type == func_called.name: # Constructor call
                        self.__quads.append((OperationCode.GOSUB, func_called.name, None, self.__operands_stack.peek().address))
                    else:
                        result = self.__temporals.next(func_called.return_type)
                        self.__quads.append((OperationCode.GOSUB, func_called.name, None, result.address))
                        self.__operands_stack.push(result)
                else:
                    self.__quads.append((OperationCode.GOSUB, func_called.name, None, None))
            
            # Check number of parameters
            param_counter = self.__param_counter_stack.pop()
            if param_counter != len(func_called.arguments):
                return (False, func_called.name, len(func_called.arguments), param_counter)
                
        return (True, None)

    def check_not_void(self, check: bool):
        func_called = self.__func_calls_stack.pop()
        
        if check and func_called.return_type == None:
            return False
        
        return True

    def add_func_return(self, expected_return_type: DataType) -> bool:
        return_val = None
        return_type = None

        if not self.__operands_stack.isEmpty():
            return_var = self.__operands_stack.pop()
            return_val = return_var.address
            return_type = return_var.var_type
        
        if expected_return_type != None:
            # Quad appended even on error to avoid also reporting 'missing return statement' on add_endproc
            self.__quads.append((OperationCode.RETURN, return_val, None, None))

        if return_type != expected_return_type:
            return False

        return True
    
    def add_endproc(self, current_func: Func) -> bool:
        self.__quads.append((OperationCode.ENDPROC, None, None, None))
        self.__temporals = Temporal()

        # Assumes last quad should be return statement
        if current_func.return_type != None:
            if current_func.return_type != current_func.name: # Not a constructor
                try:
                    if self.__quads[-2][0] != OperationCode.RETURN:
                        return False
                except IndexError: # Happens when method is blank
                    return False
        
        return True