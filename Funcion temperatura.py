temperaturas={
    "Quito":[
        [20, 22, 21, 19, 18, 17, 19], #Semana 1
        [21, 23, 20, 18, 19, 16, 17], #Semana 2
    ],
"Guayaquil": [
        [30, 31, 32, 30, 29, 28, 31],
        [32, 33, 31, 30, 29, 28, 30],
    ]
}

def promedio_temperatura(datos, ciudad, semana= None):
    """
        Calcula la temperatura promedio de una ciudad.

        Parámetros:
        - datos: diccionario con los datos de las temperaturas
        - ciudad: nombre de la ciudad (string)
        - semana: número de la semana (int, opcional).
                  Si es None, se calcula el promedio de todas las semanas.

        Retorna:
        - promedio de la temperatura (float)
        """
    if ciudad not in datos:
        raise ValueError(f"La ciudad '{ciudad}' no existe en los datos.")
    else:
        # Semana específica#
        if semana < 1 or semana > len(datos[ciudad]):
            raise ValueError(f"La ciudad '{ciudad}' solo tiene {len(datos[ciudad])} semanas registradas.")
        temperaturas_semana = datos[ciudad][semana - 1]
        return sum(temperaturas_semana) / len(temperaturas_semana)

#promedio de temperaturas de Quito de todas las semnas
    print ("Promedio de Quito (Todas las semanas ):", promedio_temperatura(temperaturas, "Quito"))
    #Promedio de Quito de la semana 1
    print("Promedio Quito (semana 1):", promedio_temperatura(temperaturas, "Quito", semana=1))
    #Promedio de Guayaquil de todas las semanas
    print("Promedio Guayaquil (todas las semanas):", promedio_temperatura(temperaturas, "Guayaquil"))

