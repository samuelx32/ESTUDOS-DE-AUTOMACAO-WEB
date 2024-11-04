import playwright 
import xlwings as xw
import pyautogui as auto
import os
import asyncio
import threading
import time


async def auto1 (wb):
    Diretorio = os.path.dirname(__file__)
    arquivo=os.path.basename(__file__)[:-3]

    from playwright.async_api import async_playwright, expect
    async with async_playwright() as p:        
        browser = await p.chromium.launch(args=["--window-position=0,0"],channel="chrome", headless=False, downloads_path=Diretorio)    
    
        CEP = await browser.new_page()
        CEP.set_default_timeout(10000)
        width = await CEP.evaluate("window.screen.width")
        height = await CEP.evaluate("window.screen.height")
        await CEP.set_viewport_size({'width': (width/2)+350, 'height': (height/2)+200})
        await CEP.goto("https://www.workana.com/pt/jobs?language=pt&skills=python") 
    
        qtn = await CEP.locator("#projects > .project-item").count()
        planilha = wb.sheets['Resultados']
        for i in range(0,qtn):
            titulo = await CEP.locator(f"#projects > .project-item > div > h2 > span > a > span >> nth = {i}").inner_text()
            planilha['workana'][i+1].value = titulo
            
            


async def auto2 (wb):
    Diretorio = os.path.dirname(__file__)
    arquivo=os.path.basename(__file__)[:-3]

    from playwright.async_api import async_playwright, expect
    async with async_playwright() as p:        
        browser = await p.chromium.launch(args=["--window-position=1000,0"],channel="chrome", headless=False, downloads_path=Diretorio)    
        
        #time.sleep(4)
        page = await browser.new_page()
        page.set_default_timeout(10000)

        width = await page.evaluate("window.screen.width")
        height = await page.evaluate("window.screen.height")
        await page.set_viewport_size({'width': (width/2)+350, 'height': (height/2)+200})
        await page.goto("https://camaranet.camara.leg.br/web/noticias-da-casa/noticias/-/resultados/avisos/10131/384295")  
        
        qtn = await page.locator(".resultados > li").count()
        planilha = wb.sheets['Resultados']
        for i in range(0,qtn):
            noticia = await page.locator(f".resultados > li >> nth = {i} ").inner_text()
            planilha['camara'][i+1].value = noticia
            
                  


async def rodar():    
    diretorio = os.path.dirname(__file__)
    arquivo = os.path.basename(__file__)[:-3]

    dir = f'{diretorio}\\{arquivo}.xlsm'
    wb = xw.Book(dir)  

    await asyncio.gather(
        auto1(wb),
        auto2(wb)
    )
    
    

    #ou
    #tarefa1=asyncio.create_task(auto1(wb))  
    #tarefa2=asyncio.create_task(auto2(wb))  

    #await tarefa1
    #await tarefa2
    
    




def main():
    asyncio.run(rodar())
    
 

if __name__ == '__main__':
    main()