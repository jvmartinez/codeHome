import componentTableData as componentData
def typeComponentTable(structuWrite, typeComponent, nameComponent, targerComponent):
    print "Componente: ", structuWrite.name
    targerComponent
    targerComponent = " ".join(targerComponent).replace("-","-*").split("-")
    print "targer"
    targerComponent.remove(targerComponent[0])
    sizeFila = targerComponent[1].replace("*","")
    targerComponent.remove(targerComponent[1])
    targerComponent = " ".join(targerComponent).split("*")
    targerComponent.remove(targerComponent[0])
    targerComponent = " ".join(targerComponent).split(" ")
    print targerComponent
    print sizeFila
    if(typeComponent =="table"):
        structuWrite.write("<table id ='" + nameComponent + "'>\n")
        headerTable(targerComponent[0],targerComponent[1],structuWrite)
        structuWrite.write("</table>\n")
        componentData.rowData(sizeFila,targerComponent[1], nameComponent)

def headerTable(sizeHeader,infoHeader,structuWrite):
    structuWrite.write("<tr>\n")
    for hearder in infoHeader.split(","):
        structuWrite.write("\t<td>\n")
        structuWrite.write("\t\t<p>"+hearder+"</p>\n")
        structuWrite.write("\t</td>\n")
    structuWrite.write("</tr>\n")