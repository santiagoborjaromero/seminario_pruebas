
import os
import csv
from src.tools.func import errorHandle, log, verificaRepositorios, PATH_DIR_FILES_SOURCE, PATH_DIR_FILES_OBJECT
     
# ------------------------------------------------------------------------------
# CONSTANTES Y VARIABLES
# ------------------------------------------------------------------------------
verificaRepositorios()

log("INFO","------------------------------------------------------------------------------")
log("INFO","PIPELINE INICIO")

archivos = ["movie.csv", "rating.csv", "tag.csv"]
log("INFO",f"Archivos {archivos}")

# ------------------------------------------------------------------------------
# PASO 1. PROCESAR UNICODE
#   Identifica caracteres unicode y los ignora permitiendo crear un nuevo archivo
#   limpio de unicode.
# ------------------------------------------------------------------------------

for archivo in archivos:
    # ------------------------------------------------------------------------------
    # Eliminar el archivos si ya existe en la carpeta destino 
    # ------------------------------------------------------------------------------
    
    if os.path.exists(PATH_DIR_FILES_OBJECT + archivo):
        log("INFO",f"Eliminando archivo destino {PATH_DIR_FILES_OBJECT + archivo}")
        os.remove(PATH_DIR_FILES_OBJECT + archivo)
        
    # ------------------------------------------------------------------------------
    # Leer archivo origen y codificar el contenido ignorando caracteres UNICODE
    # ------------------------------------------------------------------------------
    
    log("INFO",f"UNICODE Inicio proceso de limpieza del archivo {PATH_DIR_FILES_SOURCE + archivo}")
    
    try:
        with open(PATH_DIR_FILES_SOURCE + archivo, 'r', encoding='utf-8') as infile:
            content = infile.read()
            content = content.encode('windows-1252', errors='ignore')
    except Exception as e:
        errorHandle(f"(1A) {e}")
    
    
    # ------------------------------------------------------------------------------
    # Decodificar nuevamente el contenido del archivo y guardar enhun nuevo
    # ------------------------------------------------------------------------------
    try:
        openfile = open(PATH_DIR_FILES_OBJECT + archivo, "a", encoding="utf-8")
        openfile.write(content.decode('windows-1252'))
        openfile.close()    
        log("INFO",f"UNICODE Fin proceso de limpieza y creacion del archivo { PATH_DIR_FILES_OBJECT + archivo}")
    except Exception as e:
        errorHandle(f"(1B) {e}")


# ------------------------------------------------------------------------------
# STEP 2. Trabajar con archivos limpios de UNICODE
# ------------------------------------------------------------------------------



log("INFO","PIPELINE FIN")