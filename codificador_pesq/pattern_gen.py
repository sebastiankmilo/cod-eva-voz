import array,sys,random

num_bits=535 #paquetes
nporcen=[3,5,10,20,30,50,70,90]
for z in range(0, 8):
    porcen=nporcen[z]
    num_ceros=int(num_bits*0.01*porcen)

    q=1

    while(q<=50):
        k = 0
        patron=[1]*num_bits
        ceros=random.sample(range(1,num_bits), num_ceros)

        while(k<=num_ceros-1):

            patron[ceros[k]]=0
            k+=1

        a = array.array("H", patron)#prepara el archivo


        with open("pattern_"+str(num_bits)+'_'+str(porcen)+"_"+str(q)+".bin", "wb") as f: #crea
            a.tofile(f)


        q+=1
