"""
Ejercicio 1:
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos. La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""

def convertidor(h,m,s):
    s1= h*60*60
    s2= m*60
    s3= s
    segundos_totales= s1+s2+s3
    print("\nLa cantidad de segundos que hay en ese tiempo es de: " + str(segundos_totales))



def desconvertidor(j):
    horas= j//3600
    if j%3600<60:
        minutos=0
        segundos=j%3600
    else:
        minutos=(j%3600)//60
        segundos=(j%3600)%60
    print("\nHoras= " + str(horas), "\nMinutos=" + str(minutos), "\nSegundos= " + str(segundos))
    
    
convertidor(1,1,1)
desconvertidor(3661)