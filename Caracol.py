# -*- coding: cp1252 -*-
def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]]
    ##return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")

  
def der(lab,fil,col,cz,fz,n,a,h):
    
    if(col<=cz):
        for x in cargar_archivo(lab)[fil][col]:
            print x 
            #print fil, 
            der(lab,fil, (col+1),cz,fz,n,a,h)
    else:
        if((cz!=a and fz!=n )):
           # print 'FIN der', cz, fz,n,a
            down(lab,(fil+1),(col-1), (cz-1),fz, (n+1),a,h)
        else:
            if(h==0):
                down(lab,(fil+1),(col-1), (cz-1),fz, (n+1),a, (h+1))
            else:
                print 'FIN Recorrido'
             
def down(lab,fil,col,cz,fz,n,a,h):
    #print'Fil', fil, 'col', col
    if(fil<=fz ):
        for x in cargar_archivo(lab)[fil][col]:
            print x 
            down(lab,(fil+1), col, cz,fz,n,a,h)
    else:
        if ((cz!=a and fz!=n ) ):
            
            #print 'FIN down',  cz, fz,n,a  
            izq(lab,(fil-1), (col-1), (cz), (fz),n,a, h)
        else:
            if (h==0):
                izq(lab,(fil-1), (col-1), (cz), (fz),n,a, (h+1))
            else:
                print 'FIN Recorrido'
            

def izq(lab,fil,col,cz,fz,n,a,h):
    #print 'col', col, 'Fil', fil, 'fz', fz, 'IZQ'
    if(col>= (0+a)  ):
        for x in cargar_archivo(lab)[fil][col]:
            print x
    
            izq(lab,fil, (col-1),cz,fz,n,a,h)
    else:
    #    print 'col', col, 'Fil', fil
        if ((cz!=a and fz!=n ) ) :
            #print 'FIN izq', cz, fz,n,a    
            up(lab,(fil-1),(col+1),(cz),(fz-1),n, (a+1), h)
        else:
            if(h==0):
                up(lab,(fil-1),(col+1),(cz),(fz-1),n, (a+1), (h+1))
            else:
                print 'FIN Recorrido'

def up(lab,fil,col,cz,fz,n,a,h):
   # print 'col', col, 'Fil', fil, 'fz', fz
    if(fil>= (0+n) ):
        for x in cargar_archivo(lab)[fil][col]:
            print x 
           
            up(lab,(fil-1), col,cz,fz,n,a,h)
    else:
       # print 'fin UP' ,(fil+1) ,(col+1)
        if ( (cz!=a and fz!=n ) ):
            der(lab, (fil+1), (col+1), cz,(fz),n,a,h)
        else:
            if(h==0):
                der(lab, (fil+1), (col+1), cz,(fz),n,a, (h+1))
            else:
                print 'FIN Recorrido'
        
def lon(lab):
    return len(cargar_archivo("carac.txt")[0])-1   


def caracol(carac):
    der(carac,0,0,lon(carac),lon(carac),0,0,0)
    #down(carac, 0,0)
    #izq(carac, 0,3)
    #up(carac, 3,0)

#print len(cargar_archivo("carac.txt")[0])-1
caracol("carac.txt")
#print cargar_archivo("carac.txt")
#print lon("carac.txt")



# -*- coding: cp1252 -*-
