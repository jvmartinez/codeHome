import typeFunctions as funtionsPhp
def typeClass(structuWrite,_variables,funciones,nameClass):
    print "Nombre del archivo php: ", structuWrite.name
    header(structuWrite)
    structuWrite.write("class "+nameClass+"{\n")
    variables(_variables,structuWrite)
    get(_variables,structuWrite)
    set(_variables,structuWrite)
    funtionsPhp.functions(funciones,structuWrite)
    structuWrite.write("} \n")

def separator(structuWrite):
    structuWrite.write("\n")

def variables(_variables,structuWrite):
    for var in _variables:
        var = "".join(var).strip()
        structuWrite.write("\tprivate $_"+var+";\n")

def get(_variables, structuWrite):
    for getVar in _variables:
        getVar = "".join(getVar).strip()
        structuWrite.write("\tpublic function Get"+getVar+"(){\n")
        structuWrite.write("\t\t return $this->_"+getVar+";\n")
        structuWrite.write("\t}\n")
        separator(structuWrite)

def set(_variables, structuWrite):
    for getVar in _variables:
        getVar = "".join(getVar).strip()
        structuWrite.write("\tpublic function Set"+getVar+"($"+getVar+"){\n")
        structuWrite.write("\t\t $this->_"+getVar+" = $"+getVar+";\n")
        structuWrite.write("\t}\n")
        separator(structuWrite)

def header(structuWrite):
    structuWrite.write("/**\n")
    structuWrite.write("* @autor: Juan Martinez\n")
    structuWrite.write("* @framework: codeHome\n")
    structuWrite.write("* @descripcion: framework desarrollado por Juan Martinez\n")
    structuWrite.write("* @Redes Sociales: twitter | facebook | instagram @jvmartin3z\n")
    structuWrite.write("*/\n")