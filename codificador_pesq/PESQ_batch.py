import subprocess
import csv, operator

nporcen=[3,5,10,20,30,50,70,90]
arch_orig="m2"

output=[]
oaux=0
for z in range(0, 8):
    porcen=nporcen[z]
    archivo=open(arch_orig+"_"+str(porcen)+".csv","w")
    q=1
    while(q<=50):

        oaux = subprocess.check_output(["PESQ_plus.exe","+8000",arch_orig,arch_orig+"_"+str(porcen)+"_"+str(q)+"_decoded"])
        oaux=float(oaux)
        if(oaux<0):
            oaux=0
        print str(arch_orig)+str(porcen)+"Archivo No {}: {}".format(q,oaux)#muestra en que archivo va y valor del most
        output.append(oaux)
        archivo.write(str(oaux) + '\n')

        q+=1

    print len(output)
    print output
    #archivo.write(str(oaux)+'\n')

    promedio=sum(output)/len(output)
    print "\nEl promedio es\n"
    print promedio
    output.pop(0)