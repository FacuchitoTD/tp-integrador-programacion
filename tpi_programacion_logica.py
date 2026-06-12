import csv

def normalizar(texto):
    """Elimina tildes para comparación."""
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'a',
        'É': 'e',
        'Í': 'i',
        'Ó': 'o',
        'Ú': 'u'
    }
    texto = texto.lower()
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)
    return texto

def cargar_paises(ruta_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios con los datos.
    Cumple con el requerimiento de controlar errores de formato.
    """
    lista_paises = []
    
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # csv.DictReader lee cada fila directamente como un diccionario
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'].strip().title(),
                        'poblacion': int(fila['poblacion'].strip()),
                        'superficie': int(fila['superficie'].strip()),
                        'continente': fila['continente'].strip().title()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Advertencia: Fila con formato inválido omitida: {fila}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")
    
    return lista_paises

def agregar_pais(lista_paises, nombre, poblacion, superficie, continente):
    """
    Agrega un nuevo país a la lista en memoria (RAM) y lo persiste
    inmediatamente al final del archivo CSV usando el modo de apertura 'a'.
    """

    try:
        # 1. Creamos el diccionario para mantener la lista en memoria actualizada
        nuevo_pais = {
            'nombre': nombre.strip(),
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente.strip()
        }
        lista_paises.append(nuevo_pais)
        
        # 2. Abrimos el archivo en modo append ('a') para escribir al final
        # Usamos newline='' para evitar que en algunos sistemas deje renglones vacíos de más
        with open('paises.csv', mode='a', encoding='utf-8', newline='') as archivo:
            # Formateamos la cadena con los datos separados por coma
            linea_csv = f"{nuevo_pais['nombre']},{nuevo_pais['poblacion']},{nuevo_pais['superficie']},{nuevo_pais['continente']}\n"
            archivo.write(linea_csv)
            
        print(f"País '{nombre}' agregado y guardado en 'paises.csv' exitosamente.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'paises.csv' al intentar guardar.")

def actualizar_pais(lista_paises, nombre, nueva_poblacion, nueva_superficie):
    """
    Actualiza población y superficie de un país en memoria y reescribe el CSV completo.
    Retorna True si encontró el país, False si no existe.
    """
    encontrado = False
    for pais in lista_paises:
        if pais['nombre'] == nombre:
            pais['poblacion'] = nueva_poblacion
            pais['superficie'] = nueva_superficie
            encontrado = True
            break

    if not encontrado:
        return False

    try:
        with open('paises.csv', mode='w', encoding='utf-8', newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
            writer.writeheader()
            writer.writerows(lista_paises)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'paises.csv' al intentar guardar.")

    return True

def buscar_pais(lista_paises, nombre):
    """
    Busca países cuyo nombre contenga el texto ingresado.
    Retorna una lista con los países que coinciden.
    """
    resultados = []
    for pais in lista_paises:
        if normalizar(nombre) in normalizar(pais['nombre']):
            resultados.append(pais)
    return resultados

#------Todas estas 3 funciones pertenecen a la opción número 5------#
def filtrar_por_continente(lista_paises, continente):
    """
    Filtra la lista de países por continente.
    Retorna una lista con los países que coinciden.
    """
    resultados = []
    for pais in lista_paises:
        if normalizar(pais['continente']) == normalizar(continente):
            resultados.append(pais)
    return resultados
def filtrar_por_poblacion(lista_paises, minimo, maximo):
    """
    Filtra la lista de países por rango de población.
    Retorna una lista con los países cuya población está entre minimo y maximo.
    """
    resultados = []
    for pais in lista_paises:
        if minimo <= pais['poblacion'] <= maximo:
            resultados.append(pais)
    return resultados
def filtrar_por_superficie(lista_paises, minimo, maximo):
    """
    Filtra la lista de países por rango de superficie.
    Retorna una lista con los países cuya superficie está entre minimo y maximo.
    """
    resultados = []
    for pais in lista_paises:
        if minimo <= pais['superficie'] <= maximo:
            resultados.append(pais)
    return resultados
#------Fin de la opción número 5------#

def ordenar_paises(lista_paises, criterio, ascendente=True):
    """
    Ordena la lista de países según el criterio indicado.
    Retorna una nueva lista ordenada sin modificar la original.
    criterio: 'nombre', 'poblacion' o 'superficie'
    ascendente: True para ascendente, False para descendente
    """
    def obtener_valor(pais):
        return pais[criterio]

    lista_ordenada = sorted(lista_paises, key=obtener_valor, reverse=not ascendente)
    return lista_ordenada

def obtener_estadisticas(lista_paises):
    """
    Calcula y retorna un diccionario con las estadísticas del dataset.
    """
    # País con mayor y menor población
    pais_mayor_poblacion = lista_paises[0]
    pais_menor_poblacion = lista_paises[0]
    total_poblacion = 0
    total_superficie = 0
    paises_por_continente = {}

    for pais in lista_paises:
        # Mayor y menor población
        if pais['poblacion'] > pais_mayor_poblacion['poblacion']:
            pais_mayor_poblacion = pais
        if pais['poblacion'] < pais_menor_poblacion['poblacion']:
            pais_menor_poblacion = pais

        # Acumulamos para promedios
        total_poblacion += pais['poblacion']
        total_superficie += pais['superficie']

        # Contamos por continente
        continente = pais['continente']
        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1

    cantidad = len(lista_paises)

    return {
        'pais_mayor_poblacion': pais_mayor_poblacion,
        'pais_menor_poblacion': pais_menor_poblacion,
        'promedio_poblacion': total_poblacion // cantidad,
        'promedio_superficie': total_superficie // cantidad,
        'paises_por_continente': paises_por_continente
    }
