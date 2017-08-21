#! /usr/bin/env python
from array import array
import setting.Constant as constant
import lib.create as create
print "" \
      "Bienvenido a CodeHome\n" \
      "Version: 0.1\n" \
      "Desarrollador: Juan Martinez\n" \
      "Framewok:\n CodeHome esta destinado para facilitar la construccion de estructura" \
      "en php.\n" \
      "Usabilidad:\n Comando codeHelp-es(Spanish)/codeHepl-en(English) breve guia de ayuda para construir tus clases en php\n" \
      "*************************************************************************************\n" \
      ""
comand = raw_input("Instruction to execute: ")
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

if action == "codeHelp-es":
    print "Construccion de clases :\n Comienza (create class) seguido por el nombre de la clase\n"
    print "Construccion de variables:\n Comienza con (_) seguido por el nombre de la variable\n"
    print "Construccion de metodos sin parametros:\n Comienza con (:) seguido por el nombre del metodo\n"
    print "Construccion de metodos con parametros:\n Comienza con (:) seguido por el nombre del metodo y las variables \n identificada por * segida por su nombre\n"
    print "Ejemplo :create class Juan _name _lastName _sex _age :greet *friend :bye\n"

if action =="codeHelp-en":
    print "Class construction :\n Begins(create class) followed by the name of the class\n"
    print "Variables construction:\n Begins con (_) followed by the name of the variable\n"
    print "Method construction without parameters:\n Begins con (:) followed by the name of the method\n"
    print "Method construction with parameters:\n Begins con (:) followed by the name of the method and variables \n identified by * followed by name\n"
    print "Example :create class Juan _name _lastName _sex _age :greet *friend :bye\n"
else :
    if action != "create" and action != "update" and action != "delete" and action != "create-controller":
        print "Verifique que sus instrucciones sean correctas!"
        print "Ayuda instrodusca codeHome help!"
    else:
        if action.endswith("create"):
            create.create(operator, variables, actionFunctions, "none", "none")
        print "Process with success...."
