"""
Ejercicio 2:
Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:

Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos. Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.
"""

def tiempo(h,m,s):
    if h==0 and m==0:
        horas= s//3600
        if s%3600<60:
            minutos=0
            segundos=s%3600
        else:
            minutos=(s%3600)//60
            segundos=(s%3600)%60
        print("\nHoras= " + str(horas), "\nMinutos=" + str(minutos), "\nSegundos= " + str(segundos))
    else:
        s1= h*60*60
        s2= m*60
        s3= s
        segundos_totales= s1+s2+s3
        print("\nLa cantidad de segundos que hay en ese tiempo es de: " + str(segundos_totales))

tiempo(0,1,1)