import setting.Constant as constant
def functions(funciones,structuWrite):
    parametro = ""
    for func in funciones:
       parametro = parametro.join(func)
       p = parametro.find("*")
       if(p != -1):
           parametro = parametro.replace("*","*{0}")
           metodo = parametro.split("*")[0]
           parametro = parametro.split("*")
           parametro.remove(parametro[0])
           parametro = "".join(parametro).format("$").strip().replace(" ",",")
           functionsWithParameter(metodo,parametro,structuWrite)
       else:
           metodo = func
           functionWithoutParameter(metodo,structuWrite)
       parametro = ""

def functionsWithParameter(metodo,parameter,structuWrite):
    structuWrite.write("\t"+constant.functionPublic()+ metodo + "("+parameter+"){\n")
    structuWrite.write("\t\t/* Estructura del metodo */\n")
    structuWrite.write("\t}\n")

def functionWithoutParameter(metodo,structuWrite):
    structuWrite.write("\t"+constant.functionPublic()+ metodo +"(){\n")
    structuWrite.write("\t\t/* Estructura del metodo */\n")
    structuWrite.write("\t}\n")