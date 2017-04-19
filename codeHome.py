from array import array
import setting.Constant as constant
import lib.create as create

# comand = "create class juan _nombre _apellido _sexo _edad :saludar *x *y :despedir"
# comand = "create component table tableUser #miTablee -3 col1,col2,col3 -2"

print "" \
      "Bienvenido a CodeHome\n" \
      "Version: 0.1\n" \
      "Desarrollador: Juan Martinez\n" \
      "Framewok: CodeHome esta destinado para facilitar la construccion de estructura" \
      "en php.\n" \
      "Usabilidad:Comando codeHelp es breve manual de ayuda para construir tus clases en php\n" \
      "*************************************************************************************\n" \
      ""
comand = raw_input("Instruccion a ejecutar:")
tpVariables = comand
action = tpVariables.split(" ")[0]
tpVariables = tpVariables.split("_")
operator = tpVariables[0].split(" ")
actionFunctions = comand.split(":")
variables = actionFunctions[0].split("_")
actionFunctions.remove(actionFunctions[0])
operator.remove(operator[0])
variables.remove(variables[0])


def infoApp():
    document = open(constant.infoApp(), "r")
    contents = document.read()
    document.close()
    return contents

if action == "codeHelp":
    print "Construccion de clases : (create class) segido por el nombre de la clase\n"
    print "Construccion de variables comienza con (_) segido por el nombre de la variable\n"
    print "Construccion de metodos sin parametros comienza con (:) segido por el nombre del metodo\n"
    print "Construccion de metodos con parametros comienza con (:) segido por el nombre del metodo y las variables " \
          "identificada por * segida por su nombre\n"
    print "Ejemplo :create class Juan _name _lastName _sex _age :greet *friend :bye\n"
else:
    if action != "create" and action != "update" and action != "delete" and action != "create-controller":
        print "Verifique que sus instrucciones sean correctas!"
        print "Ayuda instrodusca codeHome help!"
    else:
        if action.endswith("create"):
            create.create(operator, variables, actionFunctions, "none", "none")
        if action.endswith("update"):
            print "actualizando"
        if action.endswith("delete"):
            print "eliminado"
        if action.endswith("create-controller"):
            create.create(operator, variables, actionFunctions, infoApp(), constant.controller())
        if action.endswith("create-model"):
            create.create(operator, variables, actionFunctions, infoApp(), constant.model())
        if action.endswith("create-view"):
            create.create(operator, variables, actionFunctions, infoApp(), constant.view())
        print "proceso con exito"
