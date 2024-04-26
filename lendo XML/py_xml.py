import pandas as pd
import os
import sys
import xml.etree.ElementTree as ET
import re

def extrair_nome(string):
    padrao = r'MOTORISTA:+(.*?)CPF'
    correspondencia = re.search(padrao, string)
    if correspondencia:
        return correspondencia.group(1)
    else:
        return None
    
def extrair_carreta(string):
    padrao = r'PLACA DA CARRETA:+(.*?)PLACA DO CAVALO:'
    correspondencia = re.search(padrao, string)
    if correspondencia:
        return correspondencia.group(1)
    else:
        return None
    
def extrair_cavalo(string):
    padrao = r'PLACA DO CAVALO:+(.*?)CNPJ'
    correspondencia = re.search(padrao, string)
    if correspondencia:
        return correspondencia.group(1)
    else:
        return None
    


dir = os.path.dirname(__file__)
root = ET.parse(f'{dir}\\arqxml.xml').getroot()
nsNFE = {'ns': 'http://www.portalfiscal.inf.br/nfe'}

chave = root.find('ns:NFe/ns:infNFe',nsNFE).attrib['Id'][3:]
dados = root.find('ns:NFe/ns:infNFe/ns:infAdic/ns:infCpl',nsNFE).text

nome = extrair_nome(dados)
carreta = extrair_carreta(dados)
cavalo = extrair_cavalo(dados)

print("\n\nNome: ",nome,"\nCarreta: ",carreta,"\nCavalo: ",cavalo,"\nChave: ", chave)