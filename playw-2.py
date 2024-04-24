from playwright.sync_api import sync_playwright
import time

with sync_playwright as p:
    browser = p.chromium.launch(headless=False)
    pagina = browser.new_page()
    pagina.goto("https://www.google.com/intl/pt-PT/gmail/about/")