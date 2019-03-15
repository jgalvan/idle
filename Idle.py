from antlr4 import *
from grammar.IdleLexer import IdleLexer
from grammar.IdleListener import IdleListener
from grammar.IdleParser import IdleParser
import sys

def main(argv):
    if(len(argv) != 2):
        print("usage: python Idle.py <fileName>")
        sys.exit(1)

    try:
        lexer = IdleLexer(FileStream(argv[1]))
    except:
        print("Unexpected error:", sys.exc_info()[1])
        sys.exit(1)

    stream = CommonTokenStream(lexer)
    parser = IdleParser(stream)
    tree = parser.fileState()

    if(parser.getNumberOfSyntaxErrors()):
        print("Please fix errors.")
    else:
        print("Parsed succesfully!")

if __name__ == '__main__':
    main(sys.argv)