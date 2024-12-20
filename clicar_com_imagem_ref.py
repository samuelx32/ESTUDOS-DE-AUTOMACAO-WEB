import pyautogui as auto

#instalar biblioteca opencv-python

localizacao = auto.locateOnScreen("path_imagem_referencia", confidence=0.8)

if localizacao:
    # Obtém as coordenadas centrais do elemento
    centro = auto.center(localizacao)
    # Clica nas coordenadas centrais
    auto.click(centro)
    print("Clique realizado com sucesso!")
else:
    print("Imagem não encontrada na tela.")