from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Acesse o shadow root do elemento principal
    print_preview_app = page.query_selector("print-preview-app")
    shadow_root_1 = print_preview_app.evaluate("element => element.shadowRoot")
    
    # Navegue até o próximo nível no shadow root
    print_preview_sidebar = page.evaluate(
        "root => root.querySelector('print-preview-sidebar')", shadow_root_1
    )
    shadow_root_2 = page.evaluate("element => element.shadowRoot", print_preview_sidebar)
    
    # Continue navegando para o próximo nível
    print_preview_button_strip = page.evaluate(
        "root => root.querySelector('print-preview-button-strip')", shadow_root_2
    )
    shadow_root_3 = page.evaluate("element => element.shadowRoot", print_preview_button_strip)
    
    # Localize o botão de ação
    action_button = page.evaluate(
        "root => root.querySelector('.action-button')", shadow_root_3
    )
    shadow_root_4 = page.evaluate("element => element.shadowRoot", action_button)
    
    # Localize o botão "Salvar"
    salvar_button = page.evaluate(
        "root => root.querySelector('//*[contains(text(), \"Salvar\")]')", shadow_root_4
    )
    print("Botão Salvar encontrado:", salvar_button)

    # ou

    salvar_button = page.locator(
        "print-preview-app >> print-preview-sidebar >> print-preview-button-strip >> .action-button:text('Salvar')"
    )
    salvar_button.click()
    
    browser.close()