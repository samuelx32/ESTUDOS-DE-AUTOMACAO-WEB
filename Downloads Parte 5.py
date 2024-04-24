from playwright.sync_api import Playwright, sync_playwright, expect
import os
import requests


def download_arquivo():
    with sync_playwright() as playwright:
        Diretorio=os.path.dirname(__file__)

        browser = playwright.chromium.launch(headless=False, downloads_path=Diretorio)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.borland.com/testsite/download_testpage.php")
        page.get_by_text("attachment", exact=True).click()
        with page.expect_download() as download_info:
            page.get_by_role("button", name="Download").click()
        download = download_info.value
        download.save_as("download.pdf")
        #download.save_as(f"{Diretorio}\download.pdf")

        ## download é excluído automaticamente ao final da rotina.
        #download.delete()

        # ---------------------
        context.close()
        browser.close()


#download_arquivo()
    

def download_arquivo_nova_guia():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.borland.com/testsite/download_testpage.php")
        page.get_by_text("attachment", exact=True).click()
        page.get_by_text("Open in new window", exact=True).click()
        with page.expect_download() as download_info:
            #with page.expect_popup() as page1_info:
                page.get_by_role("button", name="Download").click()
            #page1 = page1_info.value
        download = download_info.value
        #page1.close()

        download.save_as("download.pdf")

        # ---------------------
        context.close()
        browser.close()

#download_arquivo_nova_guia()


def download_link_direto():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.borland.com/testsite/download_testpage.php")
        page.get_by_role("button", name="Download").click()
        
        url_file=page.url   

        file=requests.get(url_file)

        with open("download.pdf", "wb") as f:
                f.write(file.content)
                    
        # ---------------------
        context.close()
        browser.close()

#download_link_direto()


def download_direto_link_nova_aba():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.borland.com/testsite/download_testpage.php")
        page.get_by_text("Open in new window", exact=True).click()
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="Download").click()
        page1 = page1_info.value

        url_file=page1.url   

        file=requests.get(url_file)

        with open("download.pdf", "wb") as f:
                f.write(file.content)

        # ---------------------
        context.close()
        browser.close()


download_direto_link_nova_aba()