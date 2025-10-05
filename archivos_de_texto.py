file_name= "my_notes.txt" #creamos un archivo

archivo_escritura= open(file_name, "w")#Abrimos el archivo en modo escritura"w"

archivo_escritura.write("linea 1: Mi Nombre es Steven Paredes.\n")
archivo_escritura.write("linea 2: Esta es mi ultima tarea de progrmacion en el primer semestre\n")
archivo_escritura.write("linea 3: Mi gata se llama Nina de Jesus Paredes.\n")

#Escribimos el contenido linea por linea

archivo_escritura.close() #Cerramos el archivo de escritura

#Abrimos el archivo en modo lectura "r"
archivo_lectura= open(file_name, "r")

#Mostramos el archivo para verificar
contenido_completo = archivo_lectura.read()
print("Contenido completo usando read():")
print(contenido_completo)

#Cerramos el archivo de lectura
archivo_lectura.close()