import subprocess
num_bits=535 #paquetes
porcen=90
arch_orig="m2"

nporcen=[3,5,10,20,30,50,70,90]
for z in range(0, 8):
    q = 1
    porcen=nporcen[z]
    while(q<=50):
        subprocess.call(["Codificador_iLBC.exe","20",arch_orig,"None",arch_orig+"_"+str(porcen)+"_"+str(q)+"_decoded","pattern_"+str(num_bits)+'_'+str(porcen)+"_"+str(q)+".bin"])
        q+=1