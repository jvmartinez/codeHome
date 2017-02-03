from array import array
import setting.Constant as constant
import lib.create as create
#comand = "create class juan _nombre _apellido _sexo _edad :saludar *x *y :despedir"
print "" \
      "Bienvenido a CodeHome\n"\
      "Version: 0.1\n" \
      "Desarrollador: Juan Martinez\n" \
      "Framewok: CodeHome esta destinado para facilitar la construccion de estructura" \
      "en php.\n" \
      "Usabilidad:Comando codeHelp es breve manual de ayuda para construir tus clases en php\n" \
      "*************************************************************************************\n" \
      ""
comand = raw_input("Instruccion a ejecutar:")
#comand = "create component table tableUser #miTablee -3 col1,col2,col3 -2"
tuplaVaribales = comand
action = tuplaVaribales.split(" ")[0]
tuplaVaribales = tuplaVaribales.split("_")
operador = tuplaVaribales[0].split(" ")
funciones = comand.split(":")
variables = funciones[0].split("_")
funciones.remove(funciones[0])
operador.remove(operador[0])
variables.remove(variables[0])

def infoApp():
    archivo = open(constant.infoApp(), "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

if(action == "codeHelp"):
    print "Construccion de clases : (create class) segido por el nombre de la clase\n"
    print "Construccion de variables comienza con (_) segido por el nombre de la variable\n"
    print "Construccion de metodos sin parametros comienza con (:) segido por el nombre del metodo\n"
    print "Construccion de metodos con parametros comienza con (:) segido por el nombre del metodo y las variables " \
          "identificada por * segida por su nombre\n"
    print "Ejemplo :create class Juan _name _lastName _sex _age :greet *friend :bye\n"
else:
    if(action != "create" and action != "update" and action != "delete" and action != "create-controller"):
        print "Verifique que sus instrucciones sean correctas!"
        print "Ayuda instrodusca codeHome help!"
    else:
        if (action.endswith("create")):
            create.create(operador, variables ,funciones,"none","none")
        if (action.endswith("update")):
             print "actualizando"
        if (action.endswith("delete")):
            print "eliminado"
        if (action.endswith("create-controller")):
            create.create(operador,variables,funciones,infoApp(),constant.controller())
        if (action.endswith("create-model")):
            create.create(operador,variables,funciones,infoApp(),constant.model())
        if (action.endswith("create-view")):
            create.create(operador,variables,funciones,infoApp(),constant.view())
        print "proceso con exito"
