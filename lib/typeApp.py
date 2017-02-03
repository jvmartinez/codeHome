import os
import setting.Constant as constants
def createApp(nameApp):
    print "Preparando el app: ", nameApp
    os.mkdir(nameApp, 0o777)
    os.mkdir(nameApp+constants.separador()+constants.controller())
    os.mkdir(nameApp + constants.separador() + constants.model())
    os.mkdir(nameApp + constants.separador() + constants.view())
    os.mkdir(nameApp + constants.separador() + constants.resource())
    os.mkdir(nameApp + constants.separador() + constants.resourceJs())
    os.mkdir(nameApp + constants.separador() + constants.resourceCss())
    os.mkdir(nameApp + constants.separador() + constants.resourceImg())
    createTxt(nameApp)
def createTxt(nameApp):
    txt = open(constants.infoApp(), 'w')
    txt.write(nameApp+'\n')
    txt.close()