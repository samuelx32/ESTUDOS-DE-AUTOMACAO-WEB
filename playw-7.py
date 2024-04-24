import pyautogui as auto
import os
import xlwings as xw
from playwright.sync_api import Playwright, sync_playwright, expect

@xw.sub
def chamada_python():

    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3]
    dir = f'{diretorio}\\{arquivo}.xlsm'

    wb = xw.Book(dir)
    planilha = wb.sheets["Plan1"]

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(5000)
        page.goto("file:///C:/Users/p_702809/Downloads/Ambiente de Treinamento Prático (2).html")

        tabela = page.locator("#tableUsuariosAtivos > tbody")
        linhas = tabela.locator("tr").count()
        colunas = tabela.locator("tr").first.locator("td").count()

        for linha in range(1,linhas+1):
            for coluna in range(1,colunas+1):
                elemento = tabela.locator("tr").nth(linha-1).locator("td").nth(coluna-1)
                wb.sheets["Plan1"][linha,coluna-1].value = elemento.text_content()

       
        

        auto.alert("Sistema Exectado.")
        # ---------------------
        context.close()
        browser.close()




