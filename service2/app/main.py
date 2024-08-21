from fastapi import FastAPI
import logging
import time
import threading

app = FastAPI()

# Configuración del logger
logging.basicConfig(filename='/var/log/service2/app.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def log_message():
    while True:
        logger.info("Este es un mensaje de log desde el servidor 2")
        time.sleep(5)


# Iniciar el hilo de logging en segundo plano
thread = threading.Thread(target=log_message)
thread.daemon = True
thread.start()


@app.get("/")
def read_root():
    return {"message": "Servidor 2 funcionando"}
