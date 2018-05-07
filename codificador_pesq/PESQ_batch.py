import subprocess
import csv, operator

porcen=5
arch_orig="hombres_1"
q=1
output=[]
oaux=0
archivo=open("datos1.csv","w")

while(q<=50):

    oaux = subprocess.check_output(["PESQ_plus.exe","+8000",arch_orig,arch_orig+"_"+str(porcen)+"_"+str(q)+"_decoded"])
    oaux=float(oaux)
    if(oaux<0):
        oaux=0
    print "Archivo No {}: {}".format(q,oaux)#muestra en que archivo va y valor del most
    output.append(oaux)

    q+=1

print len(output)
print output
archivo.write(output)
archivo.write('\n')

promedio=sum(output)/len(output)
print "\nEl promedio es\n"
print promedio