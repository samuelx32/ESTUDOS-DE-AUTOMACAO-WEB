import tkinter as tk
from tkinter import ttk
import time

def calculo():
    return 1+1

def processar_etapa():
    global i
    global qtn
    if i > qtn:
        splash.destroy()
        return

    
    barra_progresso["value"] = i
    splash.update_idletasks()

    i += 1
    splash.after(100, processar_etapa)  # agenda próxima etapa em 100ms

def configuracoes_da_janela():
    global splash, barra_progresso, i,qtn
    qtn = 666
    i = 0
    splash = tk.Tk()
    splash.title("Carregando...")
    splash.geometry("300x150")
    splash.overrideredirect(True)

    # Centraliza na tela
    largura = 300
    altura = 150
    largura_tela = splash.winfo_screenwidth()
    altura_tela = splash.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    splash.geometry(f"{largura}x{altura}+{x}+{y}")

    tk.Label(splash, text="Carregando, aguarde...", font=("Arial", 12)).pack(pady=20)
    barra_progresso = ttk.Progressbar(splash, length=200, mode='determinate', maximum=100)
    barra_progresso.pack(pady=10)

    # Inicia o processamento logo após a janela abrir
    
    splash.after(100, processar_etapa)
        
    splash.mainloop()

def main():
    configuracoes_da_janela()


main()
