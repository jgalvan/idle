from enum import Enum

class OperationCode(Enum):
    """Enum to represent options for operations"""

    FAKEBOTTOM = '('

    # Relops
    AND = '&&'
    EQUAL = '=='
    GE = '>='
    GT = '>'
    LE = '<='
    LT = '<'
    NOTEQUAL = '!='
    OR = '||'

    # Arithmetic operators
    ADD = '+'
    SUB = '-'
    DIV = '/'
    MULT = '*'

    # Assign
    ASSIGN = '='

    # Functions
    READINT = 'READINT'
    READFLOAT = 'READFLOAT'
    READSTRING = 'READSTRING'
    PRINT = 'PRINT'

    # Jumps
    GOTO = 'GOTO'
    GOTOF = 'GOTOF'
    GOTOT = 'GOTOT'

    # Function calls
    ERA = 'ERA'
    PARAM = 'PARAM'
    PARAMREF = 'PARAMREF'
    GOSUB = 'GOSUB'
    RETURN = 'RETURN'
    ENDPROC = 'ENDPROC'

    ARRACCESS = 'ARRACCESS'
    ARRINDEXCHECK = 'ARRINDEXCHECK'


    @staticmethod
    def from_code(code: int) -> 'OperationCode':
        """Retrieves a specific operation in OperationCode from its integer code."""

        return list(OperationCode.__members__.values())[code]

    def to_code(self):
        """Converts a specific operation in OperationCode to its integer code."""

        # TODO: Return code instead of string. String is for debugging.
        return self.value #list(OperationCode.__members__.values()).index(self)
    
    @staticmethod
    def is_relop(oper) -> bool:
        """Checks if current OperationCode is a relop"""

        return oper in [OperationCode.AND, OperationCode.EQUAL, OperationCode.GE, OperationCode.GT, OperationCode.LE, OperationCode.LT, OperationCode.NOTEQUAL, OperationCode.OR]

    @staticmethod
    def is_add_sub(oper) -> bool:
        """Checks if current OperationCode is addition or substraction"""

        return oper in [OperationCode.ADD, OperationCode.SUB]

    @staticmethod
    def is_div_mult(oper) -> bool:
        """Checks if current OperationCode is divition or multiplication"""

        return oper in [OperationCode.DIV, OperationCode.MULT]