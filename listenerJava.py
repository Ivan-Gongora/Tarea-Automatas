from sumaPruebaListener import sumaPruebaListener
from sumaPruebaParser import sumaPruebaParser

class listenerJava(sumaPruebaListener):
    def __init__(self):
        self.java_code = []
        self.java_code.append("public class Output {\n")
        self.java_code.append("    public static int multiplica(int a, int b) {\n")

    def enterAssignment(self, ctx: sumaPruebaParser.AssignmentContext):
        variable_name = ctx.IDENTIFIER().getText()
        expression = self.visit(ctx.expression())
        self.java_code.append(f"        int {variable_name} = {expression};\n")

    def enterReturnStatement(self, ctx: sumaPruebaParser.ReturnStatementContext):
        return_value = self.visit(ctx.expression())
        self.java_code.append(f"        return {return_value};\n")

    def enterPrintStatement(self, ctx: sumaPruebaParser.PrintStatementContext):
        print_value = self.visit(ctx.expression())
        self.java_code.append(f"        System.out.println({print_value});\n")

    def exitProg(self, ctx: sumaPruebaParser.ProgContext):
        self.java_code.append("    }\n")
        self.java_code.append("    public static void main(String[] args) {\n")
        self.java_code.append("        System.out.println(multiplica(5, 6));\n")
        self.java_code.append("    }\n")
        self.java_code.append("}\n")

    def visit(self, ctx):
        if isinstance(ctx, sumaPruebaParser.AddSubContext):
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            return f"({left} {operator} {right})"
        elif isinstance(ctx, sumaPruebaParser.MulDivContext):
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            return f"({left} {operator} {right})"
        elif isinstance(ctx, sumaPruebaParser.VarContext):
            return ctx.IDENTIFIER().getText()
        elif isinstance(ctx, sumaPruebaParser.NumberContext):
            return ctx.NUMBER().getText()
        elif isinstance(ctx, sumaPruebaParser.ParensContext):
            return f"({self.visit(ctx.expression())})"
        return ""

    def writeToFile(self, filename="Output.java"):
        with open(filename, 'w') as f:
            for line in self.java_code:
                f.write(line + "\n")
        print(f"Archivo {filename} generado con éxito.")
