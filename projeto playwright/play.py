import pyautogui as auto
import os
import xlwings as xw
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from io import StringIO

@xw.sub
def play():

    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3]

    dir = f'{diretorio}\\{arquivo}.xlsm'
    wb = xw.Book(dir)
    planilha = wb.sheets['Plan1']
    usuario = planilha.api.OLEObjects("usuario").Object.Value
    senha = planilha.api.OLEObjects("senha").Object.Value

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(5000)
        page.goto("file:///C:/Users/p_702809/Codigos/projeto playwright/index.html")

        page.locator('#usuario').fill(usuario)
        page.locator('#senha').fill(senha)
        page.locator('input[type="submit"]').click()
        

        fim = planilha['processo'].end('down').row
        for i in range(1,fim):
            page.locator('#menu > a').nth(0).click()

            processo = planilha['processo'][i].value
            destinatario = planilha['destinatario'][i].value

            page.get_by_placeholder("Número do Processo").fill(processo)
            page.get_by_placeholder("Destinatário").fill(destinatario)
            page.locator("#documento").set_input_files("doc_teste.pdf")
            
            page.get_by_role("button", name="Cadastrar").click()

            page.locator('#menu > a').nth(1).click()
            page.locator('#documentos > a').nth(0).click()
            page.locator("#assinar").click()
            page.once("dialog", lambda dialog: dialog.accept()) 
            auto.alert("Assinado")
            page.locator("#voltar").click()
            

        auto.alert("Sistema Exectado.")
        # ---------------------
        context.close()
        browser.close()








