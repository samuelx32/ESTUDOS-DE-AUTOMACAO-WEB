# abrindo Google e fazendo pesquisa

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    pagina = browser.new_page()
    pagina.goto("https://www.google.com/")
    pagina.locator("#APjFqb").fill("tamanduás")
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    print("Fim")
    time.sleep(10)
