from enum import Enum

class AccessModifier(Enum):
    """Enum to represent options for access modifiers"""

    PUBLIC = "+"
    PRIVATE = "-"

    @staticmethod
    def get_access_modifier(name):
        if name[0].isupper():
            return AccessModifier.PUBLIC
        return AccessModifier.PRIVATE