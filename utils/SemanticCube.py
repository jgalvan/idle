from .DataType import DataType
from .OperationCode import OperationCode

class SemanticCube:
    """Represents arithmetic and boolean operation return types."""

    @staticmethod
    def check(oper: str, left_op: DataType, right_op: DataType) -> DataType:
        """Checks return type for operation, returns DataType.ERROR if operation is invalid."""

        cube = {
            # -------------------------------------------------
            # INT
            # -------------------------------------------------

            (OperationCode.ADD, DataType.INT, DataType.INT): DataType.INT,
            (OperationCode.ADD, DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.ADD, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.ADD, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.SUB, DataType.INT, DataType.INT): DataType.INT,
            (OperationCode.SUB, DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.SUB, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.SUB, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.DIV, DataType.INT, DataType.INT): DataType.INT,
            (OperationCode.DIV, DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.DIV, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.DIV, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.MULT, DataType.INT, DataType.INT): DataType.INT,
            (OperationCode.MULT, DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.MULT, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.MULT, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.GT, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.GT, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.GT, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.GT, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.LT, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.LT, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.LT, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.LT, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.EQUAL, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.EQUAL, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.EQUAL, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.EQUAL, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.LE, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.LE, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.LE, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.LE, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.GE, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.GE, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.GE, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.GE, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.NOTEQUAL, DataType.INT, DataType.INT): DataType.BOOL,
            (OperationCode.NOTEQUAL, DataType.INT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.NOTEQUAL, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.AND, DataType.INT, DataType.INT): DataType.ERROR,
            (OperationCode.AND, DataType.INT, DataType.FLOAT): DataType.ERROR,
            (OperationCode.AND, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.AND, DataType.INT, DataType.STRING): DataType.ERROR,

            (OperationCode.OR, DataType.INT, DataType.INT): DataType.ERROR,
            (OperationCode.OR, DataType.INT, DataType.FLOAT): DataType.ERROR,
            (OperationCode.OR, DataType.INT, DataType.BOOL): DataType.ERROR,
            (OperationCode.OR, DataType.INT, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # FLOAT
            # -------------------------------------------------

            (OperationCode.ADD, DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (OperationCode.ADD, DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.ADD, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.ADD, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.SUB, DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (OperationCode.SUB, DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.SUB, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.SUB, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.DIV, DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (OperationCode.DIV, DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.DIV, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.DIV, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.MULT, DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (OperationCode.MULT, DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (OperationCode.MULT, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.MULT, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.GT, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.GT, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.GT, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.GT, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.LT, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.LT, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.LT, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.LT, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.EQUAL, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.EQUAL, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.EQUAL, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.EQUAL, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.LE, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.LE, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.LE, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.LE, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.GE, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.GE, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.GE, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.GE, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.NOTEQUAL, DataType.FLOAT, DataType.INT): DataType.BOOL,
            (OperationCode.NOTEQUAL, DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (OperationCode.NOTEQUAL, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.AND, DataType.FLOAT, DataType.INT): DataType.ERROR,
            (OperationCode.AND, DataType.FLOAT, DataType.FLOAT): DataType.ERROR,
            (OperationCode.AND, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.AND, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            (OperationCode.OR, DataType.FLOAT, DataType.INT): DataType.ERROR,
            (OperationCode.OR, DataType.FLOAT, DataType.FLOAT): DataType.ERROR,
            (OperationCode.OR, DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            (OperationCode.OR, DataType.FLOAT, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # BOOL
            # -------------------------------------------------

            (OperationCode.ADD, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.ADD, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.ADD, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.ADD, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.SUB, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.SUB, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.SUB, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.SUB, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.DIV, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.DIV, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.DIV, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.DIV, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.MULT, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.MULT, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.MULT, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.MULT, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.GT, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.GT, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.GT, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.GT, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.LT, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.LT, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.LT, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.LT, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.EQUAL, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.EQUAL, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.EQUAL, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.EQUAL, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.LE, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.LE, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.LE, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.LE, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.GE, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.GE, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.GE, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.GE, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.NOTEQUAL, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.BOOL, DataType.BOOL): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.AND, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.AND, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.AND, DataType.BOOL, DataType.BOOL): DataType.BOOL,
            (OperationCode.AND, DataType.BOOL, DataType.STRING): DataType.ERROR,

            (OperationCode.OR, DataType.BOOL, DataType.INT): DataType.ERROR,
            (OperationCode.OR, DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            (OperationCode.OR, DataType.BOOL, DataType.BOOL): DataType.BOOL,
            (OperationCode.OR, DataType.BOOL, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # STRING
            # -------------------------------------------------

            (OperationCode.ADD, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.ADD, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.ADD, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.ADD, DataType.STRING, DataType.STRING): DataType.STRING,

            (OperationCode.SUB, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.SUB, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.SUB, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.SUB, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.DIV, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.DIV, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.DIV, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.DIV, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.MULT, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.MULT, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.MULT, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.MULT, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.GT, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.GT, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.GT, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.GT, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.LT, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.LT, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.LT, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.LT, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.EQUAL, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.EQUAL, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.EQUAL, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.EQUAL, DataType.STRING, DataType.STRING): DataType.BOOL,

            (OperationCode.LE, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.LE, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.LE, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.LE, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.GE, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.GE, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.GE, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.GE, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.NOTEQUAL, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.NOTEQUAL, DataType.STRING, DataType.STRING): DataType.BOOL,

            (OperationCode.AND, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.AND, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.AND, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.AND, DataType.STRING, DataType.STRING): DataType.ERROR,

            (OperationCode.OR, DataType.STRING, DataType.INT): DataType.ERROR,
            (OperationCode.OR, DataType.STRING, DataType.FLOAT): DataType.ERROR,
            (OperationCode.OR, DataType.STRING, DataType.BOOL): DataType.ERROR,
            (OperationCode.OR, DataType.STRING, DataType.STRING): DataType.ERROR,

        }

        return cube.get((oper, left_op, right_op), DataType.ERROR)