# Sistema de Gestión de Países

**Trabajo Práctico Integrador (TPI) - Programación I**
**Tecnicatura Universitaria en Programación - UTN (Año Lectivo 2026)**

---

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar información sobre países del mundo. El sistema permite agregar, actualizar, buscar, filtrar y ordenar países, además de generar estadísticas básicas sobre el dataset. Los datos se persisten en un archivo CSV y se cargan automáticamente al iniciar el programa.

---

## Integrantes del Equipo

| Nombre | Rol |
|---|---|
| **Facundo López** | Desarrollador Técnico |
| **Leonel Leandro Quiroga** | Documentación |

---

## Estructura del Repositorio

```
tp-integrador-programacion/
├── tpi_programacion_UI.py       # Capa de interfaz: menús, inputs y validaciones
├── tpi_programacion_logica.py   # Capa de lógica: procesamiento y persistencia
├── paises.csv                   # Dataset base de países
└── README.md                    # Este archivo
```

---

## Instrucciones de Uso

**Requisitos:** Python 3.10 o superior (se utiliza `match/case`).

**Ejecutar el programa:**
```bash
python3 tpi_programacion_UI.py
```

Al iniciar, el sistema carga automáticamente el dataset desde `paises.csv` y presenta el menú principal.

---

## Menú Principal

```
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
```

---

## Ejemplos de Uso

**Agregar un país:**
```
--- Agregar un nuevo país ---
Ingrese el nombre del país: monaco
Ingrese la población del país: 39050
Ingrese la superficie del país (km2): 2
Ingrese el continente del país: europa
País 'Monaco' agregado y guardado en 'paises.csv' exitosamente.
```

**Buscar un país:**
```
--- Buscar un país por nombre ---
Ingrese el nombre del país a buscar: arg
1 resultado(s) encontrado(s):
País                                | Población  | Superficie (km2) | Continente     |
---------------------------------------------------------------------------------------
Argentina                           | 45376763   | 2780400          | América        |
```

**Filtrar por rango de población:**
```
--- Filtrar países ---
Seleccione una opción: 2
Ingrese la población mínima: 100
Ingrese la población máxima: 100000
13 país(es) encontrado(s):
...
```

**Ordenar por población descendente:**
```
--- Ordenar países ---
Seleccione criterio: 2
Seleccione orden: 2
(muestra países de mayor a menor población)
```

**Estadísticas:**
```
--- Estadísticas ---
País con mayor población: China (1412600000)
País con menor población: Vaticano (800)
Promedio de población: 36078430
Promedio de superficie: 629317 km2

Cantidad de países por continente:
  América: 35
  Europa: 44
  Asia: 47
  África: 54
  Oceanía: 14
```

---

## Arquitectura del Proyecto

El sistema aplica una arquitectura de dos capas:

- **`tpi_programacion_UI.py`** — Interfaz de usuario. Gestiona el menú, recibe inputs, valida datos y muestra resultados.
- **`tpi_programacion_logica.py`** — Lógica de negocio. Procesa los datos, realiza búsquedas, filtros, ordenamientos y maneja la persistencia en CSV.

---

## Repositorio

[https://github.com/FacuchitoTD/tp-integrador-programacion](https://github.com/FacuchitoTD/tp-integrador-programacion)

## Video explicativo
https://youtu.be/k2V-HYU2Ppo

