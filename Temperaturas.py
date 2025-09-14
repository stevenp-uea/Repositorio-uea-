def promedio_temperatura(datos, ciudad, semana=None):

    #Calcula el promedio de temperatura de todas la semnas de cada ciudad en caso de no especificar la semana
    if ciudad not in datos:
        raise ValueError(f"La ciudad '{ciudad}' no existe en los datos.")
    if semana is None:
        todas = []
        for sem in datos[ciudad]:
            todas.extend(sem)
        return sum(todas)/len(todas)
    #Promedio de una sola semana
    else:
        temperaturas_semana = datos[ciudad][semana-1]
        return sum(temperaturas_semana)/len(temperaturas_semana)

#Se introducen los datos de dos semanas para cada ciudad
temperaturas = {
    "Quito": [
        [20, 22, 21, 19, 18, 17, 19], #Semana 1
        [21, 23, 20, 18, 19, 16, 17], #Semana 2
    ],
    "Guayaquil": [
        [30, 31, 32, 30, 29, 28, 31], #Semana 1
        [32, 33, 31, 30, 29, 28, 30], #Semana 2
    ]
}

print("Promedio Quito:", promedio_temperatura(temperaturas, "Quito"))
print("Promedio Quito semana 1:", promedio_temperatura(temperaturas, "Quito", semana=1))
print("Promedio Guayaquil:", promedio_temperatura(temperaturas, "Guayaquil"))

