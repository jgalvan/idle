from antlr4 import *
from grammar.IdleLexer import IdleLexer
from grammar.IdleListener import IdleListener
from grammar.IdleParser import IdleParser
from IdleVirtualMachine import IdleVirtualMachine
import sys

def main(argv):
    """Idle compiler main function, used to compile a file in the Idle Language.
    
    usage: python Idle.py <fileName>
    """

    # Check parameter presence
    if(len(argv) != 2):
        print("usage: python Idle.py <fileName>")
        sys.exit(1)

    # Check if file exists
    try:
        lexer = IdleLexer(FileStream(argv[1]))
    except:
        print("Unexpected error:", sys.exc_info()[1])
        sys.exit(1)

    # Parse
    stream = CommonTokenStream(lexer)
    parser = IdleParser(stream)
    tree = parser.fileState()

    # Check for errors
    errors = parser.icomp.compiler_errors
    if(len(errors) > 0):
        for error in errors:
            print(error)
        print("Please fix errors.")
    elif(parser.getNumberOfSyntaxErrors()):
        print("Please fix errors.")
    else:
        virtual_machine = IdleVirtualMachine(parser.icomp.const_quads, parser.icomp.quads)
        virtual_machine.run()

if __name__ == '__main__':
    main(sys.argv)