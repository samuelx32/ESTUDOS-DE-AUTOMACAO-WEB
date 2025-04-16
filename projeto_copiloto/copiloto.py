from threading import Thread
import pyautogui as auto
from playwright.sync_api import sync_playwright

def menu():
    op = auto.confirm(text="menu",buttons=["op1","op2"])

def main():
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com")

        auto.alert("pausa")




if __name__ == '__main__':
   
    # Iniciar menu em thread
    menu_thread = Thread(target=menu)
    menu_thread.start()

    # Rodar navegador no processo principal
    main()

    # Esperar o menu acabar
    menu_thread.join()

