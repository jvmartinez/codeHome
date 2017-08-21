import setting.Constant as constant
def functions(functions, structuWrite):
    parameter = ""
    for func in functions:
       parameter = parameter.join(func)
       p = parameter.find("*")
       if(p != -1):
           parameter = parameter.replace("*","*{0}")
           method = parameter.split("*")[0]
           parameter = parameter.split("*")
           parameter.remove(parameter[0])
           parameter = "".join(parameter).format("$").strip().replace(" ",",")
           functionsWithParameter(method,parameter,structuWrite)
       else:
           method = func
           functionWithoutParameter(method,structuWrite)
       parameter = ""

def functionsWithParameter(method, parameter, structuWrite):
    structuWrite.write("\t" + constant.functionPublic() + method + "(" + parameter + "){\n")
    structuWrite.write("\t\t/* Structure of the method */\n")
    structuWrite.write("\t}\n")

def functionWithoutParameter(method, structuWrite):
    structuWrite.write("\t" + constant.functionPublic() + method + "(){\n")
    structuWrite.write("\t\t/* Structure of the method */\n")
    structuWrite.write("\t}\n")