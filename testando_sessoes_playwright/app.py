
from playwright.sync_api import sync_playwright, expect
import os
import pyautogui as auto



diretorio = os.path.dirname(__file__)



with sync_playwright() as p:        
    browser = p.chromium.launch(channel="chromium", headless=False, downloads_path=diretorio)  
    context = browser.new_context(
    #permissions=["geolocation"],  # Permissão para acessar a localização
    #geolocation={"latitude": -23.55052, "longitude": -46.633308},  # São Paulo, Brasil
    #locale="pt-BR",  # Configura o idioma do navegador
    storage_state=f"{diretorio}\\session.json" 
    )


    page = context.new_page()
    page.goto("https://web.whatsapp.com/")
    auto.alert("faça login")

    context.storage_state(path=f"{diretorio}\\session.json")

    browser.close()