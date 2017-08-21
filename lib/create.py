import typeClass as typeClass
import setting.Constant as constant
import setting.ConstantType as constantType

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
