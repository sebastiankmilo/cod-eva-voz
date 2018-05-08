import subprocess
import csv, operator

porcen=90
arch_orig="m1"
q=1
output=[]
oaux=0
archivo=open(arch_orig+"_"+str(porcen)+".csv","w")

while(q<=50):

    oaux = subprocess.check_output(["PESQ_plus.exe","+8000",arch_orig,arch_orig+"_"+str(porcen)+"_"+str(q)+"_decoded"])
    oaux=float(oaux)
    if(oaux<0):
        oaux=0
    print "Archivo No {}: {}".format(q,oaux)#muestra en que archivo va y valor del most
    output.append(oaux)
    archivo.write(str(oaux) + '\n')

    q+=1

print len(output)
print output
#archivo.write(str(oaux)+'\n')

promedio=sum(output)/len(output)
print "\nEl promedio es\n"
print promedio