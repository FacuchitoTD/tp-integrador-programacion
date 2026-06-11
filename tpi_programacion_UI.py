import tpi_programacion_logica as logica

def mostrar_tabla_paises(lista_paises):
    """Muestra la lista de países con el formato de recuadro calibrado."""
    print(f"\n{'País':<35} | {'Población':<10} | {'Superficie (km2)':<16} | {'Continente':<15} |")
    print("-" * 87)
    
    for pais in lista_paises:
        nombre = pais['nombre']
        poblacion = pais['poblacion']
        superficie = pais['superficie']
        continente = pais['continente']
        
        print(f"{nombre:<35} | {poblacion:<10} | {superficie:<16} | {continente:<15} |")
    print("-" * 87)

def agregar_pais(lista_paises):
    """Solicita al usuario los datos de un nuevo país y lo agrega a la lista y al archivo."""
    print("\n--- Agregar un nuevo país ---")
    nombre = input("Ingrese el nombre del país: ").strip().title()
    if not nombre:
        print("Error: El nombre del país no puede estar vacío.")
        return
    poblacion = input("Ingrese la población del país: ").strip()
    try:        
        poblacion = int(poblacion)
    except ValueError:
        print("Error: La población debe ser un número entero.")
        return
    superficie = input("Ingrese la superficie del país (km2): ").strip()
    try:
        superficie = int(superficie)
    except ValueError:
        print("Error: La superficie debe ser un número entero.")
        return
    continente = input("Ingrese el continente del país: ").strip().title()
    if not continente:
        print("Error: El continente no puede estar vacío.")
        return

    # Si todo está perfecto, llama a la lógica para guardarlo
    logica.agregar_pais(lista_paises, nombre, poblacion, superficie, continente)

def actualizar_pais(lista_paises):
    """Solicita el país a actualizar y los nuevos valores de población y superficie."""
    print("\n--- Actualizar población y superficie ---")

    nombre = input("Ingrese el nombre del país a actualizar: ").strip().title()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    nueva_poblacion = input("Ingrese la nueva población: ").strip()
    try:
        nueva_poblacion = int(nueva_poblacion)
    except ValueError:
        print("Error: La población debe ser un número entero.")
        return
    if nueva_poblacion < 0:
        print("Error: La población no puede ser negativa.")
        return

    nueva_superficie = input("Ingrese la nueva superficie (km2): ").strip()
    try:
        nueva_superficie = int(nueva_superficie)
    except ValueError:
        print("Error: La superficie debe ser un número entero.")
        return
    if nueva_superficie <= 0:
        print("Error: La superficie debe ser mayor a cero.")
        return

    encontrado = logica.actualizar_pais(lista_paises, nombre, nueva_poblacion, nueva_superficie)

    if encontrado:
        print(f"País '{nombre}' actualizado exitosamente.")
    else:
        print(f"Error: No se encontró ningún país con el nombre '{nombre}'.")

def buscar_pais(lista_paises):
    """Solicita el nombre a buscar y muestra los resultados encontrados."""
    print("\n--- Buscar un país por nombre ---")
    nombre = input("Ingrese el nombre del país a buscar: ").strip().title()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    resultados = logica.buscar_pais(lista_paises, nombre)

    if not resultados:
        print(f"No se encontró ningún país con el nombre '{nombre}'.")
        return

    print(f"\n{len(resultados)} resultado(s) encontrado(s):")
    mostrar_tabla_paises(resultados)
    
def filtrar_por_continente(lista_paises):
    """Solicita un continente y muestra los países que pertenecen a él."""
    continente = input("Ingrese el continente a filtrar: ").strip().title()
    if not continente:
        print("Error: El continente no puede estar vacío.")
        return

    resultados = logica.filtrar_por_continente(lista_paises, continente)

    if not resultados:
        print(f"No se encontraron países en el continente '{continente}'.")
        return

    print(f"\n{len(resultados)} país(es) encontrado(s) en {continente}:")
    mostrar_tabla_paises(resultados)
def filtrar_por_poblacion(lista_paises):
    """Solicita un rango de población y muestra los países que coinciden."""
    minimo = input("Ingrese la población mínima: ").strip()
    try:
        minimo = int(minimo)
    except ValueError:
        print("Error: La población mínima debe ser un número entero.")
        return
    if minimo < 0:
        print("Error: La población mínima no puede ser negativa.")
        return

    maximo = input("Ingrese la población máxima: ").strip()
    try:
        maximo = int(maximo)
    except ValueError:
        print("Error: La población máxima debe ser un número entero.")
        return
    if maximo < minimo:
        print("Error: La población máxima no puede ser menor que la mínima.")
        return

    resultados = logica.filtrar_por_poblacion(lista_paises, minimo, maximo)

    if not resultados:
        print(f"No se encontraron países con población entre {minimo} y {maximo}.")
        return

    print(f"\n{len(resultados)} país(es) encontrado(s):")
    mostrar_tabla_paises(resultados)
def filtrar_por_superficie(lista_paises):
    """Solicita un rango de superficie y muestra los países que coinciden."""
    minimo = input("Ingrese la superficie mínima (km2): ").strip()
    try:
        minimo = int(minimo)
    except ValueError:
        print("Error: La superficie mínima debe ser un número entero.")
        return
    if minimo < 0:
        print("Error: La superficie mínima no puede ser negativa.")
        return

    maximo = input("Ingrese la superficie máxima (km2): ").strip()
    try:
        maximo = int(maximo)
    except ValueError:
        print("Error: La superficie máxima debe ser un número entero.")
        return
    if maximo < minimo:
        print("Error: La superficie máxima no puede ser menor que la mínima.")
        return

    resultados = logica.filtrar_por_superficie(lista_paises, minimo, maximo)

    if not resultados:
        print(f"No se encontraron países con superficie entre {minimo} y {maximo} km2.")
        return

    print(f"\n{len(resultados)} país(es) encontrado(s):")
    mostrar_tabla_paises(resultados)
def filtrar_paises(lista_paises):
    """Muestra el submenú de filtros y deriva a la función correspondiente."""
    print("""
    --- Filtrar países ---
    1. Por continente
    2. Por rango de población
    3. Por rango de superficie
    0. Volver al menú principal
    """)

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case '1':
            filtrar_por_continente(lista_paises)
        case '2':
            filtrar_por_poblacion(lista_paises)
        case '3':
            filtrar_por_superficie(lista_paises)
        case '0':
            return
        case _:
            print("Error: Opción no válida. Elija entre 0 y 3.")

def ordenar_paises(lista_paises):
    """Muestra el submenú de ordenamiento y presenta los resultados."""
    print("""
    --- Ordenar países ---
    1. Por nombre
    2. Por población
    3. Por superficie
    0. Volver al menú principal
    """)

    opcion = input("Seleccione criterio: ").strip()
    try:
        opcion = int(opcion)
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    match opcion:
        case 1:
            criterio = 'nombre'
        case 2:
            criterio = 'poblacion'
        case 3:
            criterio = 'superficie'
        case 0:
            return
        case _:
            print("Error: Opción no válida. Elija entre 0 y 3.")
            return

    print("""
    1. Ascendente
    2. Descendente
    """)

    orden = input("Seleccione orden: ").strip()
    try:
        orden = int(orden)
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    match orden:
        case 1:
            ascendente = True
        case 2:
            ascendente = False
        case _:
            print("Error: Opción no válida.")
            return

    resultado = logica.ordenar_paises(lista_paises, criterio, ascendente)
    mostrar_tabla_paises(resultado)
            
def menu_principal():
    # Cargamos el dataset al arrancar el programa
    lista_paises = logica.cargar_paises('paises.csv')
    
    while True:
        print("""
    ╔════════════════════════════════════════════════════╗
    ║             SISTEMA DE GESTIÓN DE PAÍSES           ║
    ╠════════════════════════════════════════════════════╣
    ║  1. Mostrar todos los países                       ║
    ║  2. Agregar un país                                ║
    ║  3. Actualizar población y superficie              ║
    ║  4. Buscar un país por nombre                      ║
    ║  5. Filtrar países                                 ║
    ║  6. Ordenar países                                 ║
    ║  7. Mostrar estadísticas                           ║
    ║  0. Salir del sistema                              ║
    ╚════════════════════════════════════════════════════╝
        """)

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("\nError: Ingrese un número válido.")
            continue

        match opcion:
            case '1':
                if lista_paises:
                    mostrar_tabla_paises(lista_paises)
                else:
                    print("\nNo hay países cargados en el sistema.")
                    
            case '2':
                agregar_pais(lista_paises)
                
            case '3':
                actualizar_pais(lista_paises)
                
            case '4':
                buscar_pais(lista_paises)
                
            case '5':
                filtrar_paises(lista_paises)
                
            case '6':
                ordenar_paises(lista_paises)

            case '7':
                print("\n[Próximamente] Lógica para mostrar estadísticas...")
                
            case '0':
                print("\nSaliendo del programa...")
                break
                
            case _:
                print("\nError: Opción no válida. Elija entre 0 y 7.")

if __name__ == "__main__":
    menu_principal()