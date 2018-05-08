import subprocess

porcen=90
arch_orig="m1"
q=1

while(q<=50):
    subprocess.call(["Codificador_iLBC.exe","20",arch_orig,"None",arch_orig+"_"+str(porcen)+"_"+str(q)+"_decoded","pattern_"+str(porcen)+"_"+str(q)+".bin"])
    q+=1