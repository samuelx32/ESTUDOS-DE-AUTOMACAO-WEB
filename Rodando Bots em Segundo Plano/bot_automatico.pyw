import pyautogui as auto
import threading
import time
import schedule

def minha_tarefa():
    auto.alert("Essa é uma mensagem de teste.")

def rodar_schedule():
    schedule.every().day.at("15:48").do(minha_tarefa)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Criar e iniciar a thread
thread = threading.Thread(target=rodar_schedule)
thread.daemon = True
thread.start()

while True:
    time.sleep(10)  # Simulando outras atividades no programa principal
