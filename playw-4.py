import pyautogui as auto
import os
import xlwings as xw
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("file:///C:/Users/p_702809/Downloads/Ambiente%20de%20Treinamento%20Pr%C3%A1tico.html")

    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3]

    dir = f'{diretorio}\\{arquivo}.xlsm'
    wb = xw.Book(dir)
    planilha = wb.sheets['Plan1']
    fim = planilha['Nome'].end('down').row
    for linha in range (1,fim):
        nome = planilha['Nome'][linha].value
        sobrenome = planilha['Sobrenome'][linha].value
        nome_completo = f'{nome} {sobrenome}'
        organizacao = planilha['Organizacao'][linha].value
        sexo = planilha['sexo'][linha].value
        data_nasc = planilha['data_nascimento'][linha].value
        data_nasc = format(data_nasc, "%Y-%m-%d") 
        tempo_gasto = planilha['tempo_gasto'][linha].value  
        gastos_pre = planilha['gastos_pre'][linha].value
        pos_trilha = planilha['posicao_trilha'][linha].value
        sugestao = planilha['Sugestao'][linha].value
        

        #page.get_by_label("Nome:").fill(nome_completo)
        page.locator("input[id='nome']").fill(nome_completo)

        #page.get_by_placeholder("Digite sua Organização").fill(organizacao)
        page.locator("input[id='organizacao']").fill(organizacao)

        #page.get_by_label(planilha['sexo'][linha].value).check()
        if (sexo == "Masculino"):
            page.locator("input[id='sexo0']").check()
        elif (sexo == "Feminino"):
            page.locator("input[id='sexo1']").check()

        #page.get_by_label("Data de Nascimento:").fill(data_nasc)
        page.locator("input[id='nascimento']").fill(data_nasc)

        #page.get_by_label("Tempo gasto diariamente com tarefas repetitivas:").select_option(label=tempo_gasto)
        page.locator("select[id='tempogasto']").select_option(label=tempo_gasto)


        #page.get_by_label(gastos_pre).check()
        if (gastos_pre == "Mapeamento da Rotina Maçante"):
            page.locator("input[id='fasesMetodo0']").check()
        elif (gastos_pre == "Lapidação do Esqueleto do Robô"):
            page.locator("input[id='fasesMetodo1']").check()
        elif (gastos_pre == "Integração Funcional com o Excel"):
            page.locator("input[id='fasesMetodo2']").check()
        elif (gastos_pre == "Lapidação do Esqueleto do Robô"):
            page.locator("input[id='fasesMetodo3']").check()
        

        #page.get_by_label("Em qual posição da trilha do aluno você se encontra?").select_option(label=pos_trilha)
        page.locator("select[id='trilhaAluno']").select_option(label=pos_trilha)

        #page.get_by_label("Sugestões de Cursos:").fill(sugestao)
        page.locator("textarea[id='sugestoes']").fill(sugestao)
        
        page.locator("input[id='buttonDelay']").click()
        time.sleep(2)
        page.locator("input[id='buttonSimple2']").click()
        
        teste = page.locator("div[id='resultado']").text_content()
        wb.sheets[planilha]['Resultado'][linha].value = teste
        page.get_by_role("link", name="Limpar").click()
        


    
    auto.alert("Sistema Exectado.")
    # ---------------------
    context.close()
    browser.close()




@xw.sub
def chamada_sistema():
    with sync_playwright() as playwright:
        run(playwright)



def funcoes():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("file:///C:/Users/p_702809/Downloads/Ambiente%20de%20Treinamento%20Pr%C3%A1tico.html")

        page.get_by_role("button", name="Botão Simples").click()
        time.sleep(2)
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Alert").click()
        time.sleep(2)
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Confirm").click()
        time.sleep(2)
        page.once("dialog", lambda dialog: dialog.accept("textotexto"))
        page.get_by_role("button", name="Prompt").click()
        time.sleep(2)
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Alert").click()
        time.sleep(2)
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="Popup").click()
        page1 = page1_info.value
        page1.get_by_role("textbox").fill("arraiaaa")
        page1.close()

        # ---------------------
        context.close()
        browser.close()

funcoes()




    


