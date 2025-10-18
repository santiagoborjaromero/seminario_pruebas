# UNIANDES

#### Universidad Autonoma de los Andes

## **Grupo 8**

Integrantes:

- Jaime Santiago Borja Romero
- Hugo Alfredo Herrera Villalva
- Jorge Luis López Romo

Semario Complexivo

## **Título del Proyecto**

**Construcción de un Sistema de Recomendación Híbrido de Películas.**

## **Definición del Problema**

Las recomendaciones de películas no son del todo precisas, ya que no consideran de manera adecuada variables como el sexo y la edad. En consecuencia, algunos géneros cinematográficos tienden a ser menos vistos por determinados grupos de personas.

La desconfianza en las recomendaciones de películas debido a la gran cantidad de opciones y a las reseñas poco fiables, afecta al público objetivo al dificultar la elección de contenido de calidad, haciendo crucial la solución para que los usuarios puedan satisfacer sus necesidades de manera eficiente

## **Descripción del Proyecto**


## **Herramientas Utilizadas**


## **Instrucciones**

### Proceso Pipeline

Pipeline es un proceso de limpieza de los datasets fuente, que incluye:
1. Depuracion de caracteres UNICODE creando un respaldo de los archivos dataset para poder trabajar con ellos, manteniendo la data original aislada.
2.  < Aumentar mas procesos>

Consideraciones especiales

1. Verificar que la carpeta `dataset_source` se encuentren los archivos requeridos para el proceso
2. El directorio de trabajo es `pipeline`
3. El archivo que indica los paths de carpetas para el proceso es `pipeline/src/tools/func.py`, se puede en el mismo contexto aumentar si es necesario
4. Para ejecutar el proceso 
```c
cd pipeline
python pipeline.py
```
5. Para visualizar los logs puede revisar en `pipeline/logs/srhp-{fecha}.log`

