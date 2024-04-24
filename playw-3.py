import pyautogui as auto
import os
import xlwings as xw

@xw.sub
def chamada_python():

    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3]

    #auto.alert(diretorio)
    #auto.alert(arquivo)

    dir = f'{diretorio}\\{arquivo}.xlsm'
    print(dir)
    wb = xw.Book(dir)
    for linha in range (3,8):
        nome = wb.sheets['Plan1']['Nome'][linha-1].value
        sobrenome = wb.sheets['Plan1']['Sobrenome'][linha-1].value
        wb.sheets['Plan1']['Descricao'][linha-1].value = f"O meu nome é {nome} {sobrenome}"