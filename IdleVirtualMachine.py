from utils.OperationCode import OperationCode
from virtual_machine_utils.Memory import Memory

class IdleVirtualMachine():
    def __init__(self, const_quadruples, quadruples):
        self.__const_quadruples = const_quadruples
        self.__quadruples = quadruples

    def run(self):
        self.init_consts()

        # RUN

    def init_consts(self):
        temp = Memory()

        for quad in self.__const_quadruples:
            temp.set_value(quad[1], quad[3])

        print(Memory.CONSTANTS)