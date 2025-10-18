from datetime import datetime
import os
from pathlib import Path

CURRENT_DIR = str(Path.cwd())
PATH_DIR_FILES_SOURCE = CURRENT_DIR + "/../dataset_source/"
PATH_DIR_FILES_OBJECT = CURRENT_DIR + "/dataset_object/"
PATH_DIR_FILES_LOGS   = CURRENT_DIR + "/logs/"

PATHS = [
    PATH_DIR_FILES_LOGS,
    PATH_DIR_FILES_SOURCE,
    PATH_DIR_FILES_OBJECT,
]

def verificaRepositorios():
    for directorio in PATHS:
        if not os.path.exists(directorio):
            log("INFO", f"Creando directorio {directorio}")
            os.mkdir(directorio)

def errorHandle(error_text=""):
    ## AQUI
    ## Se debe procesar el error si hay algun caso especifico con como salir y terminar el pipeline
    log("ERROR", error_text)

def log(type="INFO", text_log=""):
    dthoy =  datetime.now()
    fecha = dthoy.strftime("%Y-%m-%d %H:%M:%S")

    archivo = f"srhp-{dthoy.strftime("%Y%m%d")}.log"
    
    openfile = open(f"{PATH_DIR_FILES_LOGS}{archivo}", "a", encoding="utf-8")
    text = f"{fecha} [{type}] {text_log}"
    print(text)
    openfile.write(text + "\n")
    openfile.close()    