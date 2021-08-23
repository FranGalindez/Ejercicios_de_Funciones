"""
Ejercicio 3:
Queremos hacer una función que añada a una lista los contactos de una agenda.

Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, 
aunque puede tener más campos. Los datos se irán pidiendo por teclado,
 se pedirá de antemanos cuantos contactos se van a guardar.

Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el "*".

Ejercicio 4:
Amplía el programa anterior para hacer una función de búsqueda,
que reciba un conjunto de parámetros keyword y devuelve los contactos (en una lista) que coincidan con los criterios de búsqueda

"""

cuantos_contactos=int(input("\n¿Cuántos contactos quiere añadir?\n"))
agenda_final=[]
def agendar(cuantos_contactos):
    while cuantos_contactos>0:
        diccionario= agregar_nombre_numero_info() 
        agenda_final.append(diccionario)

        cuantos_contactos-=1
buscar_campo=[]
buscar_info=[]
def agregar_nombre_numero_info():
    diccionario_contactos = {}
    nombre=input("Ingrese el nombre del contacto:\t")
    diccionario_contactos["nombre"]=nombre
    numero=int(input("\nNúmero de teléfono del contacto:\t"))
    diccionario_contactos["numero"]=numero
    info=True
    while info==True:
        campo_adicional=input("\nSi desea agregar más info, escriba \"si\" De lo contrario, escriba \"*\" :\t")
        if campo_adicional=="si":
              agrego_campo=input("\nIngrese que campo quiere agregar:\t")
              buscar_campo.append(agrego_campo)  
              agrego_info_campo=input("\nAgregue la información del mencionado:\t")
              buscar_info.append(agrego_info_campo)
              diccionario_contactos[str(agrego_campo)]=agrego_info_campo
              info=False
        else:
            buscar_campo.append("no info") 
            buscar_info.append("no info")
            info=False
        
    return diccionario_contactos


agendar(cuantos_contactos)

print(agenda_final)
largo=len(agenda_final)


filtrado=[]
resultados = False
def buscador_contactos():
    pregunta=input("\n ¿Desea filtrar contactos? si/no\n")
    if pregunta=="si":
        campo=input("\nIngrese el campo que desea buscar:\n")
        info=input("\nIngrese la información de dicho campo:\n")
        for i in range(len(buscar_campo)):
            if campo == buscar_campo[i]:
                if info == buscar_info[i]:
                    filtrado.append(agenda_final[i])
                    resultados==True

    else:
        print("\nQue tenga un buen día =)\n")
            

                
            
buscador_contactos()
print(filtrado)
            

    