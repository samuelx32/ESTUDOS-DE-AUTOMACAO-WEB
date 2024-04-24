import pyautogui as auto
import os
import xlwings as xw
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from io import StringIO

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

        wb.sheets['Plan1']['A:D'].clear_contents()
        tabela = page.locator("#tableUsuariosAtivos > tbody")
        dados_tabela = tabela.inner_text()
        dados_tabela = pd.read_csv(StringIO(dados_tabela), sep='\t', header=None)
        wb.sheets['Plan1']['A1'].options(pd.DataFrame, header = 0, index=False,expand='table').value = dados_tabela

       
        

        auto.alert("Sistema Exectado.")
        # ---------------------
        context.close()
        browser.close()




