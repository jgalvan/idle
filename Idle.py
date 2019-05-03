from antlr4 import *
from grammar.IdleLexer import IdleLexer
from grammar.IdleListener import IdleListener
from grammar.IdleParser import IdleParser
from IdleVirtualMachine import IdleVirtualMachine
from IdleCompiler import IdleCompiler
import sys
import os

def main(argv):
    """Idle compiler main function, used to compile a file in the Idle Language.
    
    usage: python Idle.py <fileName>
    """

    # Check parameter presence
    if(len(argv) != 2):
        print("usage: python Idle.py <fileName>")
        sys.exit(1)

    file_name = argv[1]

    # Check if file exists
    try:
        lexer = IdleLexer(FileStream(file_name))
    except:
        print("Unexpected error:", sys.exc_info()[1])
        sys.exit(1)

    # Set current working directory in case there are imports
    dir_path = os.path.dirname(os.path.realpath(file_name))
    IdleCompiler.cwd = dir_path
    IdleCompiler.files_imported.append(os.path.basename(file_name).replace(".idle", ""))

    # Parse
    try:
        stream = CommonTokenStream(lexer)
        parser = IdleParser(stream)
        tree = parser.fileState()
    except Exception as e:
        # If the compiler crashed, check if we had any compiler errors
        errors = parser.icomp.compiler_errors
        if(len(errors) > 0):
            for error in errors:
                print(error)
            print("Please fix errors.")
        elif(parser.getNumberOfSyntaxErrors()):
            print("Please fix errors.")
        else:
            # Compiler crashed without any known errors, panic :'(
            raise e
        exit()

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