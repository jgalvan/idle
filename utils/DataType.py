from enum import Enum

class DataType(Enum):
    """Enum to represent options for data types"""

    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    ERROR = "error"

    @staticmethod
    def exists(name: str) -> bool:
        """Checks if data type is primitive data type."""

        for dtype in DataType.__members__.values():
            if name == dtype.value:
                return True
        
        return False
    
    def __str__(self):
        return self.value