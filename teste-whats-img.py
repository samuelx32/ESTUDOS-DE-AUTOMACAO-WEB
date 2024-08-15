import pandas as pd
import os
import sys
from datetime import datetime
import pyautogui as auto
import re
import playwright
import requests
import tkinter as tk
from tkinter import filedialog


if getattr(sys, 'frozen', False):
    diretorio = os.path.dirname(sys.executable)
    arquivo = os.path.basename(sys.executable)[:-4]
elif __file__:
    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3] 

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:  
    browser = p.chromium.launch(args=["--window-position=10,10"],channel="chrome", headless=False, downloads_path=diretorio)  
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({'width': 1220, 'height': 600})
    page.set_default_timeout(240000)
    page.goto("https://web.whatsapp.com/")
    expect(page.locator(".landing-title >> nth = 0")).to_be_visible(timeout=120000)
    expect(page.locator(".landing-title >> nth = 0")).not_to_be_visible(timeout=120000)

    telefone = '984696057'

    try:
        expect(page.locator("div[title='Nova conversa']")).to_be_visible(timeout=240000)
        page.locator("div[title='Nova conversa']").click(timeout=4000)
    except:
        expect(page.locator("span[data-icon='new-chat-outline']")).to_be_visible(timeout=240000)
        page.locator("span[data-icon='new-chat-outline']").click(timeout=4000)

    page.locator("div[role='textbox'] >> nth=0").type(telefone,delay=50)
    page.wait_for_timeout(1000)
    page.locator("div[role='button'] div[role='gridcell'] >> nth = 0").click(timeout=240000)

    page.locator("span[data-icon='plus'] > svg").click()

    page.locator("'Fotos e vídeos'").click()
    expect(page.locator("div[aria-label='Enviar']")).to_be_visible(timeout=240000)
    page.locator("div[aria-label='Enviar']").click()
    auto.alert("pause")
    

    