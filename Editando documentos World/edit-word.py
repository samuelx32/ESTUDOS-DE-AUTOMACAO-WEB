from docx import Document
import os

def main(dir):
    empresa = "GW Sistemas"
    nome = "Juriandir Golveia Santos"
    cpf = "99900099988"
    rg = "65748674"


    documento = Document(f'{dir}\\modelo-contrato.docx')
    referencias = {
        'NOMEDAEMPRESA': empresa,
        'NOME': nome,
        'CPFF': cpf,
        'RGG': rg
    }

    for paragrafo in documento.paragraphs:
        for run in paragrafo.runs:
            for ref, valor in referencias.items():
                if ref in run.text:
                    # Substitui o código de referência pelo valor correspondente
                    run.text = run.text.replace(ref, valor)
    
    documento.save(f'{dir}\\{nome}-contrato.docx')

if __name__ == "__main__":

    diretorio = os.path.dirname(__file__)
    main(diretorio)