import pyautogui as auto
import os
from playwright.sync_api import Playwright, sync_playwright, expect

def tabelas():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(5000)
        page.goto("file:///C:/Users/p_702809/Downloads/Ambiente%20de%20Treinamento%20Pr%C3%A1tico.html")

        diretorio = os.path.dirname(__file__)
        arquivo = os.path.basename(__file__)[:-3]
        total_linhas = page.locator('#tableUsuarios > tbody > tr').count()
        total_colunas = page.locator('#tableUsuarios > tbody > tr:nth-child(1) > td').count()

        for i in range (1,total_linhas+1):
            for x in range (1,total_colunas+1):
                if x == 1:
                    page.locator(f'#tableUsuarios > tbody > tr:nth-child({i}) > td:nth-child({x}) >> input').check()
                elif x == 3:
                    if page.locator(f'#tableUsuarios > tbody > tr:nth-child({i}) > td:nth-child({x}) > input').is_checked() == True:
                        aluno = True
                    else:
                        aluno = False
                elif x == 4:
                    if (aluno == True):
                        page.locator(f'#tableUsuarios > tbody > tr:nth-child({i}) > td:nth-child({x}) > input').fill("Matricula Provável")
                    else:
                        page.locator(f'#tableUsuarios > tbody > tr:nth-child({i}) > td:nth-child({x}) > input').fill("Matricula Improvável")
            


        auto.alert("Sistema Exectado.")
        # ---------------------
        context.close()
        browser.close()

tabelas()