porcen=90
arch_orig='m1'
archivo=strcat(arch_orig,'_')
archivo=strcat(archivo,int2str(porcen))
archivo=strcat(archivo,'.csv')
datos=csvread(archivo)
y=mean(datos);
v=zeros(50,1);
for k=1:50
    v(k)=y;
end
fig=figure (1)
plot(datos)
hold on
plot(v)
hold off
texto=strcat('Grafica : ',int2str(porcen))
texto=strcat(texto,' % de distorsión y 50 patrones Audio:')
texto=strcat(texto,arch_orig)
title(texto)
xlabel(strcat('promedio :',num2str(y)))
fname ='C:\Users\Usuario\Desktop\Universidad\9 semestre\Conmutacion\segundo corte\calificacióndevoz\codificador_pesq'
filename=strcat(arch_orig,'_')
filename=strcat(filename,int2str(porcen))
saveas(fig,fullfile(fname,filename),'jpeg')