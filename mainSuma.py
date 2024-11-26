from antlr4 import *
from sumaPruebaLexer import sumaPruebaLexer
from sumaPruebaParser import sumaPruebaParser
from listenerJava import listenerJava

def main():
    input_stream = FileStream("prueba.txt")
    lexer = sumaPruebaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sumaPruebaParser(stream)
    
    tree = parser.prog()

    listener = listenerJava()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    listener.writeToFile("Output.java")
    print("Archivo Output.java generado con éxito.")

if __name__ == '__main__':
    main()
