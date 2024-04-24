import pyautogui 
import os
import xlwings as xw


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    Diretorio=os.path.dirname(__file__)
    arquivo=os.path.basename(__file__)[:-3]

    diretorio_arquivo=f'{Diretorio}\\{arquivo}.xlsm'

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    #context.set_default_timeout(5000)
    page = context.new_page()
    page.set_default_timeout(5000)
    page.goto(f"file:///{Diretorio}/Ambiente de Treinamento Prático.html")   
   
    wb=xw.Book(diretorio_arquivo)
    planilha=wb.sheets['Dados']
    ultima_linha = planilha['Nome'].end('down').row

    # Css Selectors
    # nomeTag[nomeAtributo='valorAtributo']
    # nomeTag[nomeAtributo1='valorAtributo1'][nomeAtributo2='valorAtributo2']

    for linha in range(1,ultima_linha):                       

        nome=planilha['Nome'][linha].value
        sobrenome=planilha['Sobrenome'][linha].value
        nome_completo=f"{nome} {sobrenome}" 
        #page.get_by_label("Nome:").fill(nome_completo)
        #page.locator("input[id='nome']").fill(nome_completo, timeout=10000)
        page.locator("input[id='nome']").fill(nome_completo)
        #page.locator("input[id='nome'][name='nome']").fill(nome_completo)

        organizacao=planilha['Organização'][linha].value
       
        #page.get_by_placeholder("Digite sua Organização").fill(organizacao)
        page.locator("input[id='organizacao']").fill(organizacao)
        
        # sexo=planilha['Sexo'][linha].value
        # if sexo=="Masculino":
        #     #page.locator("input[id='sexo0']").check(timeout=10000)
        #     page.locator("input[id='sexo0']").check()
        # elif sexo=="Feminino":
        #     page.locator("input[id='sexo1']").check()

        page.get_by_label(planilha['Sexo'][linha].value).check()
        
        nascimento=planilha['Data_Nascimento'][linha].value
        nascimento=format(nascimento,"%Y-%m-%d")
        #page.get_by_label("Data de Nascimento:").fill(nascimento)
        page.locator("input[id='nascimento']").fill(nascimento)
        
        tempo_gasto=planilha['Tempo_Gasto'][linha].value
        #page.get_by_role("combobox", name="Tempo gasto diariamente com tarefas repetitivas:").select_option(label=tempo_gasto)
        page.locator("select[id='tempogasto']").select_option(label=tempo_gasto)

        fase_preferida=planilha['Fase_Preferida'][linha].value
        page.get_by_label(fase_preferida).check()        

        posicao_trilha=planilha['Posicao_Trilha'][linha].value        
        #page.get_by_role("combobox", name="Em qual posição da trilha do aluno você se encontra?").select_option(label=posicao_trilha) 
        page.locator("select[id='trilhaAluno']").select_option(label=posicao_trilha) 

        sugestao=planilha['Sugestão'][linha].value   
        #page.get_by_label("Sugestões de Cursos:").fill(sugestao)
        page.locator("textarea[id='sugestoes']").fill(sugestao)

        # Processar:
        page.locator("input[id='buttonDelay']").click()

        # Espera explícita:
        #page.wait_for_timeout(10000)

        # Enviar relatório:
        page.locator("input[id='buttonSimple2']").click() 

        planilha['Resultado'][linha].value = page.locator("div[id='resultado']").text_content()  
        #planilha['Resultado'][linha].value = page.locator("div[id='resultado']").inner_text() 
       
        page.get_by_role("link", name="Limpar").click()
        # #page.locator("a[onclick='javascript:limpar()']").click(timeout=10000)
        # page.locator("a[onclick='javascript:limpar()']").click()
        
    pyautogui.alert("Sistema Executado")

    context.close()
    browser.close()

@xw.sub
def executar_sistema():
    with sync_playwright() as playwright:
        run(playwright)

#executar_sistema()


from playwright.sync_api import Playwright, sync_playwright, expect

def lidando_com_elementos_especificos():
    with sync_playwright() as playwright:
        Diretorio=os.path.dirname(__file__)
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()        
        page.goto(f"file:///{Diretorio}/Ambiente de Treinamento Prático.html")

        # Lidando com PopUps:
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="Popup").click()
        page1 = page1_info.value        
        page1.get_by_role("textbox").fill("Texto")
        page1.close()

        # Lidando com Alertas:
        page.once("dialog", lambda dialog: dialog.dismiss()) # Ou dialog.accept()
        page.get_by_role("button", name="Alert").click()

        # Lidando com Confirms:
        page.once("dialog", lambda dialog: dialog.accept()) # dialog.dismiss() para clicar em Cancelar
        page.get_by_role("button", name="Confirm").click()

        # Lidando com Prompts:
        page.once("dialog", lambda dialog: dialog.accept("Texto Prompt")) # dialog.dismiss() para clicar em Cancelar
        page.get_by_role("button", name="Prompt").click()

        # Lidando com iFrames:
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.frame_locator("#frame1").get_by_role("button", name="Frame Button").click()

        # Lidando com Hover():
        page.get_by_role("button", name="Dropdown").hover()
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="Playwright").click()
        page1 = page1_info.value
       
        context.close()
        browser.close()

lidando_com_elementos_especificos()
