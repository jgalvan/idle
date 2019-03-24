from .DataType import DataType

class SemanticCube:
    """Represents arithmetic and boolean operation return types."""

    @staticmethod
    def check(oper: str, left_op: DataType, right_op: DataType) -> DataType:
        """Checks return type for operation, returns DataType.ERROR if operation is invalid."""

        cube = {
            # -------------------------------------------------
            # INT
            # -------------------------------------------------

            ('+', DataType.INT, DataType.INT): DataType.INT,
            ('+', DataType.INT, DataType.FLOAT): DataType.FLOAT,
            ('+', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('+', DataType.INT, DataType.STRING): DataType.ERROR,

            ('-', DataType.INT, DataType.INT): DataType.INT,
            ('-', DataType.INT, DataType.FLOAT): DataType.FLOAT,
            ('-', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('-', DataType.INT, DataType.STRING): DataType.ERROR,

            ('/', DataType.INT, DataType.INT): DataType.FLOAT,
            ('/', DataType.INT, DataType.FLOAT): DataType.FLOAT,
            ('/', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('/', DataType.INT, DataType.STRING): DataType.ERROR,

            ('*', DataType.INT, DataType.INT): DataType.INT,
            ('*', DataType.INT, DataType.FLOAT): DataType.FLOAT,
            ('*', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('*', DataType.INT, DataType.STRING): DataType.ERROR,

            ('>', DataType.INT, DataType.INT): DataType.BOOL,
            ('>', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('>', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('>', DataType.INT, DataType.STRING): DataType.ERROR,

            ('<', DataType.INT, DataType.INT): DataType.BOOL,
            ('<', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('<', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('<', DataType.INT, DataType.STRING): DataType.ERROR,

            ('==', DataType.INT, DataType.INT): DataType.BOOL,
            ('==', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('==', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('==', DataType.INT, DataType.STRING): DataType.ERROR,

            ('<=', DataType.INT, DataType.INT): DataType.BOOL,
            ('<=', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('<=', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('<=', DataType.INT, DataType.STRING): DataType.ERROR,

            ('>=', DataType.INT, DataType.INT): DataType.BOOL,
            ('>=', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('>=', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('>=', DataType.INT, DataType.STRING): DataType.ERROR,

            ('!=', DataType.INT, DataType.INT): DataType.BOOL,
            ('!=', DataType.INT, DataType.FLOAT): DataType.BOOL,
            ('!=', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('!=', DataType.INT, DataType.STRING): DataType.ERROR,

            ('&&', DataType.INT, DataType.INT): DataType.ERROR,
            ('&&', DataType.INT, DataType.FLOAT): DataType.ERROR,
            ('&&', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('&&', DataType.INT, DataType.STRING): DataType.ERROR,

            ('||', DataType.INT, DataType.INT): DataType.ERROR,
            ('||', DataType.INT, DataType.FLOAT): DataType.ERROR,
            ('||', DataType.INT, DataType.BOOL): DataType.ERROR,
            ('||', DataType.INT, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # FLOAT
            # -------------------------------------------------

            ('+', DataType.FLOAT, DataType.INT): DataType.FLOAT,
            ('+', DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            ('+', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('+', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('-', DataType.FLOAT, DataType.INT): DataType.FLOAT,
            ('-', DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            ('-', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('-', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('/', DataType.FLOAT, DataType.INT): DataType.FLOAT,
            ('/', DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            ('/', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('/', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('*', DataType.FLOAT, DataType.INT): DataType.FLOAT,
            ('*', DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            ('*', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('*', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('>', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('>', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('>', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('>', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('<', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('<', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('<', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('<', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('==', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('==', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('==', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('==', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('<=', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('<=', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('<=', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('<=', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('>=', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('>=', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('>=', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('>=', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('!=', DataType.FLOAT, DataType.INT): DataType.BOOL,
            ('!=', DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            ('!=', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('!=', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('&&', DataType.FLOAT, DataType.INT): DataType.ERROR,
            ('&&', DataType.FLOAT, DataType.FLOAT): DataType.ERROR,
            ('&&', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('&&', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            ('||', DataType.FLOAT, DataType.INT): DataType.ERROR,
            ('||', DataType.FLOAT, DataType.FLOAT): DataType.ERROR,
            ('||', DataType.FLOAT, DataType.BOOL): DataType.ERROR,
            ('||', DataType.FLOAT, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # BOOL
            # -------------------------------------------------

            ('+', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('+', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('+', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('+', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('-', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('-', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('-', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('-', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('/', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('/', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('/', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('/', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('*', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('*', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('*', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('*', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('>', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('>', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('>', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('>', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('<', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('<', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('<', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('<', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('==', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('==', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('==', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('==', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('<=', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('<=', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('<=', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('<=', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('>=', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('>=', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('>=', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('>=', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('!=', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('!=', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('!=', DataType.BOOL, DataType.BOOL): DataType.ERROR,
            ('!=', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('&&', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('&&', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('&&', DataType.BOOL, DataType.BOOL): DataType.BOOL,
            ('&&', DataType.BOOL, DataType.STRING): DataType.ERROR,

            ('||', DataType.BOOL, DataType.INT): DataType.ERROR,
            ('||', DataType.BOOL, DataType.FLOAT): DataType.ERROR,
            ('||', DataType.BOOL, DataType.BOOL): DataType.BOOL,
            ('||', DataType.BOOL, DataType.STRING): DataType.ERROR,

            # -------------------------------------------------
            # STRING
            # -------------------------------------------------

            ('+', DataType.STRING, DataType.INT): DataType.ERROR,
            ('+', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('+', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('+', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('-', DataType.STRING, DataType.INT): DataType.ERROR,
            ('-', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('-', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('-', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('/', DataType.STRING, DataType.INT): DataType.ERROR,
            ('/', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('/', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('/', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('*', DataType.STRING, DataType.INT): DataType.ERROR,
            ('*', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('*', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('*', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('>', DataType.STRING, DataType.INT): DataType.ERROR,
            ('>', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('>', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('>', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('<', DataType.STRING, DataType.INT): DataType.ERROR,
            ('<', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('<', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('<', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('==', DataType.STRING, DataType.INT): DataType.ERROR,
            ('==', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('==', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('==', DataType.STRING, DataType.STRING): DataType.BOOL,

            ('<=', DataType.STRING, DataType.INT): DataType.ERROR,
            ('<=', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('<=', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('<=', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('>=', DataType.STRING, DataType.INT): DataType.ERROR,
            ('>=', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('>=', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('>=', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('!=', DataType.STRING, DataType.INT): DataType.ERROR,
            ('!=', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('!=', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('!=', DataType.STRING, DataType.STRING): DataType.BOOL,

            ('&&', DataType.STRING, DataType.INT): DataType.ERROR,
            ('&&', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('&&', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('&&', DataType.STRING, DataType.STRING): DataType.ERROR,

            ('||', DataType.STRING, DataType.INT): DataType.ERROR,
            ('||', DataType.STRING, DataType.FLOAT): DataType.ERROR,
            ('||', DataType.STRING, DataType.BOOL): DataType.ERROR,
            ('||', DataType.STRING, DataType.STRING): DataType.ERROR,

        }

        return cube.get((oper, left_op, right_op), DataType.ERROR)