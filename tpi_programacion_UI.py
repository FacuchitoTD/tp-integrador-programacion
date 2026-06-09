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
                print("\n[Próximamente] Lógica para buscar por nombre...")
                
            case '5':
                print("\n[Próximamente] Lógica para filtrar...")
                
            case '6':
                print("\n[Próximamente] Lógica para ordenar...")
                
            case '7':
                print("\n[Próximamente] Lógica para mostrar estadísticas...")
                
            case '0':
                print("\nSaliendo del programa...")
                break
                
            case _:
                print("\nError: Opción no válida. Elija entre 0 y 7.")

if __name__ == "__main__":
    menu_principal()