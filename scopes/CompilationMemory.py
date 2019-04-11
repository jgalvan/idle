from .Variable import *
from utils.DataType import DataType

class CompilationMemory():
    CONSTANTS = {
        DataType.INT: dict(),
        DataType.FLOAT: dict(),
        DataType.BOOL: dict(),
        DataType.STRING: dict()
    }

    
    # SCOPE TYPE
    CONSTANT_ID = 1
    INSTANCE_ID = 2
    LOCAL_ID = 3
    TEMP_ID = 4

    # VARIABLE TYPE
    VAR_TYPE = {
        DataType.INT: 1,
        DataType.FLOAT: 2,
        DataType.BOOL: 3,
        DataType.STRING: 4,
        'Other': 5
    }

    VAR_TYPE_FROM_CODE = {
        1: DataType.INT,
        2: DataType.FLOAT,
        3: DataType.BOOL,
        4: DataType.STRING,
        5: 'Other'
    }

    def __init__(self):
        self.int_counter = 0
        self.float_counter = 0
        self.bool_counter = 0
        self.string_counter = 0
        self.obj_counter = 0
        self.scope_type = CompilationMemory.LOCAL_ID

    @staticmethod
    def get_constant(value, var_type: DataType) -> Variable:
        const_dict = CompilationMemory.CONSTANTS.get(var_type)
        
        var = const_dict.get(value, None)

        if var == None:
            address = len(const_dict) + 1
            address = address*10 + CompilationMemory.VAR_TYPE.get(var_type, CompilationMemory.VAR_TYPE['Other'])
            address = address*10 + CompilationMemory.CONSTANT_ID

            if var_type == DataType.STRING:
                value = CompilationMemory.clean_string_const(value)

            var = Variable(value, var_type, address)
            const_dict.update({value: var})

        return var

    @staticmethod
    def clean_string_const(value):
        return value[1:-1]

    def get_next_address(self, var_type: DataType):
        postfix = CompilationMemory.VAR_TYPE.get(var_type, CompilationMemory.VAR_TYPE['Other'])*10 + self.scope_type
        
        if var_type == DataType.INT:
            self.int_counter += 1
            return (self.int_counter)*100 + postfix
        elif var_type == DataType.FLOAT:
            self.float_counter += 1
            return (self.float_counter)*100 + postfix
        elif var_type == DataType.BOOL:
            self.bool_counter += 1
            return (self.bool_counter)*100 + postfix
        elif var_type == DataType.STRING:
            self.string_counter += 1
            return (self.string_counter)*100 + postfix
        else:
            self.obj_counter += 1
            return (self.obj_counter)*100 + postfix

class Temporal(CompilationMemory):
    def __init__(self):
        CompilationMemory.__init__(self)
        self.__availables = {
            DataType.INT: [],
            DataType.FLOAT: [],
            DataType.BOOL: [],
            DataType.STRING: []
        }
        self.scope_type = CompilationMemory.TEMP_ID
        
    def next(self, var_type: DataType):
        available = self.__availables.get(var_type, []) # Default is object. Object temporals should always be new

        if len(available) > 0:
            next_var = available.pop()
            return next_var
        
        address = self.get_next_address(var_type)
        next_var = Variable(address, var_type, address)
        return next_var

    @staticmethod
    def is_temp(var):
        return var.address % 10 == CompilationMemory.TEMP_ID

    def free_up_if_temp(self, var):
        if Temporal.is_temp(var):
            available = self.__availables.get(var.var_type, []) # Default is object. Object temporals should always be new
            available.append(var)
