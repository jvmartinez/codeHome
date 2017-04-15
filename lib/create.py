import typeClass as typeClass
import setting.Constant as constant
import setting.ConstantType as constantType
import typeComponet as typeComponent
import typeApp as app


def create(_class, variable, functions, infoApp, path):
    if _class[0] == constant.class_():
        if infoApp == "none":
            fo = open(_class[1] + constantType.php(), "wb")
        else:
            if path == constant.controller():
                url = infoApp.strip() + "/" + path + "/" + _class[1] + constantType.php()
            fo = open(url, "wb")
        fo.write(constant.phpBegin() + "\n")
        typeClass.typeClass(fo, variable, functions, _class[1])
        fo.write(constant.phpEnd() + "\n")
        fo.close()

    if _class[0] == constant.component():
        confComponent = " ".join(_class).split("#")
        confComponent.remove(confComponent[0])
        fo = open(_class[2] + constantType.html(), "wb")
        fo.write(constant.divBegin() + "\n")
        if (_class[1] == constant.table()):
            typeComponent.typeComponentTable(fo, _class[1], _class[2], confComponent)
        fo.write(constant.divEnd() + "\n")
        fo.close()
    if _class[0] == constant.app():
        app.createApp(_class[1])
