def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]]
    ##return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")

ele =[]
def road(elem):
    ele.append(elem)
    
def der(lab,fil,col):
    
    if(col<=lon(lab) and (cargar_archivo(lab)[fil][col] in ele)==False ):
        for x in cargar_archivo(lab)[fil][col]:
            print x , 'derecha'
            #print fil, col
            road(x)
            der(lab,fil, (col+1))
    else:
        #print ele, '-----------'
        #print fil, col
        if((cargar_archivo(lab)[fil+1][col-1] in ele)==False):
            down(lab,(fil+1),(col-1))
        else:
             print 'FIN der'
#        der(lab,fil,(col+1))

def down(lab,fil,col):
    #print'Fil', fil, 'col', col
    if(fil<=lon(lab) and (cargar_archivo(lab)[fil][col] in ele)==False ):
        for x in cargar_archivo(lab)[fil][col]:
            print x , 'down'
            road(x)
            down(lab,(fil+1), col)
    else:
        if( (cargar_archivo(lab)[fil-1][col-1] in ele)==False ):
            
            izq(lab,(fil-1), (col-1))
        else:
            print 'FIN down'

def izq(lab,fil,col):
    if(col>=0 and (cargar_archivo(lab)[fil][col] in ele)==False):
        for x in cargar_archivo(lab)[fil][col]:
            print x , 'izq'
            road(x)
            izq(lab,fil, (col-1))
    else:
    #    print 'col', col, 'Fil', fil
        if( (cargar_archivo(lab)[fil-1][col+1] in ele)==False ):
            
            up(lab,(fil-1),(col+1))
        else:
            print 'FIN izq'

def up(lab,fil,col):
    #print 'col', col, 'Fil', fil
    if(fil>=0 and (cargar_archivo(lab)[fil][col] in ele)==False ):
        for x in cargar_archivo(lab)[fil][col]:
            print x , 'up'
            road(x)
            up(lab,(fil-1), col)
    else:
       # print 'fin UP' ,(fil+1) ,(col+1)
        if ((cargar_archivo(lab)[fil+1][col+1] in ele)==False):
            der(lab, (fil+1), (col+1))
        else:
            print 'FIN up'
        
def lon(lab):
    return len(cargar_archivo("carac.txt")[0])-1   



def caracol(carac):
    der(carac,0,0)
    #down(carac, 0,0)
    #izq(carac, 0,3)
    #up(carac, 3,0)

#print len(cargar_archivo("carac.txt")[0])-1
caracol("carac.txt")
#print cargar_archivo("carac.txt")
print ele
#print lon("carac.txt")

    
