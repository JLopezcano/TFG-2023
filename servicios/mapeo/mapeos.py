from clases.classes import data

def getArrayIndex(arg, index):
    aux=[]
    
    for a in arg:
        aux.append(a[index])
    return aux
    
def format(arg,type):
    for a in arg:
        index = arg.index(a)
        arg[index] = float(a)

    if type == data.position:
        arg.pop()
        arg.pop()
        arg.remove(arg[1])
        return arg
    if type == data.light:
        arg.remove(arg[3])
        arg.remove(arg[1])
        return arg