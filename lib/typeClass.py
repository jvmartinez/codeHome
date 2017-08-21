import typeFunctions as funtionsPhp
def typeClass(structuWrite, _variables, functions, nameClass):
    print "Name file php: ", structuWrite.name
    header(structuWrite)
    structuWrite.write("class "+nameClass+"{\n")
    variables(_variables,structuWrite)
    get(_variables,structuWrite)
    set(_variables,structuWrite)
    funtionsPhp.functions(functions, structuWrite)
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
        structuWrite.write("\tpublic function get"+getVar.capitalize()+"(){\n")
        structuWrite.write("\t\t return $this->_"+getVar+";\n")
        structuWrite.write("\t}\n")
        separator(structuWrite)

def set(_variables, structuWrite):
    for getVar in _variables:
        getVar = "".join(getVar).strip()
        structuWrite.write("\tpublic function set"+getVar.capitalize()+"($"+getVar+"){\n")
        structuWrite.write("\t\t $this->_"+getVar+" = $"+getVar+";\n")
        structuWrite.write("\t}\n")
        separator(structuWrite)

def header(structuWrite):
    structuWrite.write("/**\n")
    structuWrite.write("* @Author: Juan Martinez\n")
    structuWrite.write("* @Framework: codeHome\n")
    structuWrite.write("* @Description: framework developed by Juan Martinez\n")
    structuWrite.write("* @Social networks: (twitter) =>  @jvmartin3z\n")
    structuWrite.write("* @Social networks: (gitHub) =>  @jvmartinez\n")
    structuWrite.write("*/\n")