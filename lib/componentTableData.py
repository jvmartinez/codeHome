import json
def rowData(sizeRows,sizecols,nameComponent):
    h = {}
    print sizecols.split(",")
    d = sizecols.split(",")
    print range(int(sizeRows))
    for i in range(int(sizeRows)):
        h[i] = d
    with open(nameComponent+".json", 'wb') as outfile:
        json.dump(h, outfile)