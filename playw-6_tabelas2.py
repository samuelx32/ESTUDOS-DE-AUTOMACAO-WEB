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

        tabela = page.locator('#tableUsuarios > tbody')
        total_linhas = tabela.locator('tr').count()
        linhas = tabela.locator("tr").all()

        for linha in linhas:
            elementos = linha.locator("td").locator("input").all()
            for elemento in elementos:
                if elemento.get_attribute("type") == "radio":
                    elemento.check()
                elif elemento.get_attribute("type") == "checkbox":
                    if elemento.is_checked() == True:
                        aluno = True
                    else:
                        aluno = False
                elif elemento.get_attribute("type") == "text":
                    if (aluno == True):
                        elemento.fill("Matricula Provável")
                    else:
                        elemento.fill("Matricula Improvável")
            


        auto.alert("Sistema Exectado.")
        # ---------------------
        context.close()
        browser.close()

tabelas()