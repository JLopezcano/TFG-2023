arrayGlobal=[]
lista=["aaaaa","bbbb",["cccc", "ddd"],["eee"]]

def recursiva(listado):
    auxReturn=[]
    auxResponsive=[]
    for element in listado:
        print(element)
        print(isinstance(element,str))
        if isinstance(element,str):
            print("Guardado")
            auxReturn.append(element)
        else:
            auxResponsive.append(element)
    print("a.a.a",auxResponsive)
        
    if len(auxResponsive) != 0:
        for rec in auxResponsive:
            print("rec",rec)
            a=recursiva(rec)
            print("for",auxResponsive)
            auxResponsive.remove(rec)
            for b in a:
                auxReturn.append(b)
                print("auxReturn",auxReturn)          
            print("a-a",auxResponsive)
    else: return auxReturn
        

    
#arrayGlobal=recursiva(lista)   
print("Global",arrayGlobal)    

pru="asdf"
def ffff(prueba,index):
    if(len(prueba)!=index):
        print(prueba[index])
        ffff(prueba,index+1)
    else: print("fin")

ffff(pru,0)
    
    
    
    
    