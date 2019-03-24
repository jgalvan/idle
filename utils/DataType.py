from enum import Enum

class DataType(Enum):
    """Enum to represent options for data types"""

    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    ERROR = "error"

    @staticmethod
    def exists(name) -> bool:
        for dtype in DataType.__members__.values():
            if name == dtype.value:
                return True
        
        return False