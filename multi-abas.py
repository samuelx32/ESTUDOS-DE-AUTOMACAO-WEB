from playwright.sync_api import sync_playwright
import pyautogui as auto

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Abre a primeira aba
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://www.google.com/")
    page2.goto("https://www.google.com/")
    page1.locator("#APjFqb").fill("canguru")
    page1.keyboard.press("Enter")
    page2.locator("#APjFqb").fill("tamanduás")
    page2.keyboard.press("Enter")

    auto.alert("pause")

    browser.close()