import sys
import re

def ribosome(N1,N2,N3):
#Esta función sirve como la tabla del código genético, recibe 3 nucleótidos y regresa el aminoácido que codifica el codon.
    if((N1=="U" and N2=="U") and (N3=="U" or N3=="C")):
        print("F",end=" ")
    if((N1=="U" and N2=="U") and (N3=="A" or N3=="G")):
        print("L",end=" ")
    if((N1=="C" and N2=="U") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("L",end=" ")
    if((N1=="A" and N2=="U") and (N3=="U" or N3=="C" or N3=="A")):
        print("I",end=" ")
    if((N1=="A" and N2=="U") and (N3=="G")):
        print("M",end=" ")
    if((N1=="G" and N2=="U") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("V",end=" ")
    if((N1=="U" and N2=="C") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("S",end=" ")
    if((N1=="C" and N2=="C") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("P",end=" ")
    if((N1=="A" and N2=="C") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("T",end=" ")
    if((N1=="G" and N2=="C") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("A",end=" ")
    if((N1=="U" and N2=="A") and (N3=="U" or N3=="C")):
        print("Y",end=" ")
    if((N1=="U" and N2=="A") and (N3=="A" or N3=="G")):
        print("STOP",end=" ")
    if((N1=="C" and N2=="A") and (N3=="U" or N3=="C")):
        print("H",end=" ")
    if((N1=="C" and N2=="A") and (N3=="A" or N3=="G")):
        print("Q",end=" ")
    if((N1=="A" and N2=="A") and (N3=="U" or N3=="C")):
        print("N",end=" ")
    if((N1=="A" and N2=="A") and (N3=="A" or N3=="G")):
        print("K",end=" ")
    if((N1=="G" and N2=="A") and (N3=="U" or N3=="C")):
        print("D",end=" ")
    if((N1=="G" and N2=="A") and (N3=="A" or N3=="G")):
        print("E",end=" ")
    if((N1=="U" and N2=="G") and (N3=="U" or N3=="C")):
        print("C",end=" ")
    if((N1=="U" and N2=="G") and (N3=="A")):
        print("STOP",end=" ")
    if((N1=="U" and N2=="G") and (N3=="G")):
        print("W",end=" ")
    if((N1=="C" and N2=="G") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("R",end=" ")
    if((N1=="A" and N2=="G") and (N3=="U" or N3=="C")):
        print("S",end=" ")
    if((N1=="A" and N2=="G") and (N3=="A" or N3=="G")):
        print("R",end=" ")
    if((N1=="G" and N2=="G") and (N3=="A" or N3=="G" or N3=="U" or N3=="C")):
        print("G",end=" ")
#Recibimos los parámetros de la consola y la guardamos en una lista
arguments=sys.argv[1:]
sequence=list(arguments[0])
length=len(sequence)
#Con este bloque de código hacemos evaluaciones a la secuencia introducida.
if re.search(r'[^AUCG|aucg]',arguments[0]):
    print("MAKE SURE TO INTRODUCE THE CORRECT NUCLEOTIDES (A,U,C,G)")
    sys.exit(1)
if length % 3:
    print("SEQUENCE LENGTH MUST BE A MULTIPLE OF 3")
    sys.exit(1)

#Creamos un for que recorra la lista y leyendo por codones llame a la función ribosoma que imprimirá el aminoácido correspondiente.
print("\n Amino acid sequence:")
for i in range(0,length,3):
    ribosome(sequence[i].upper(),sequence[i+1].upper(),sequence[i+2].upper())
print("\n")
