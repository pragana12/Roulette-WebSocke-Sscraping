from playwright.sync_api import sync_playwright, expect

import time

def capture_websocket_url():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        import re

        # Função para capturar e imprimir a URL do WebSocket
        def log_ws_requests(ws):
            if ws.url.startswith("wss://esportesdasorte.evo-games.com/public/roulette/player/game/") and "messageFormat=json" in ws.url:
                # Substituir a parte da URL por {id_roleta}
                modified_url = re.sub(r"(game/)[^/]+(/socket)", r"\1{id_roleta}\2", ws.url)
                print(f"WS Request URL: {modified_url}")
                with open('/home/user/scrap/captured_urls.txt', 'w') as file:
                    file.write(modified_url)
                print(f"Urls capturadas salvas em captured_urls.txt")
                return modified_url  # Retorna a URL do WebSocket
                

        # Intercepta as requisições WebSocket
        page.on('websocket', log_ws_requests)

        # Navega para a página desejada
        page.goto("https://www.esportesdasorte.com/ptb/bet/main")
        print('Abriu o esporte da sorte')
        page.get_by_role("textbox", name="Usuário").click()
        page.get_by_role("textbox", name="Usuário").fill("seu usuario")
        page.get_by_role("textbox", name="Senha").click()
        page.get_by_role("textbox", name="Senha").fill("sua senha")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_role("button", name="Login")).not_to_be_visible()
        print('fez o login')
        page.goto("https://www.esportesdasorte.com/ptb/games/livecasino/detail/normal/20952/evol_PorROU0000000001_BRL")
        print('entrou na roleta')
        time.sleep(10)
        # Tira uma captura de tela e salva no arquivo 'screenshot.png'
        page.screenshot(path="screenshot.png")
        # Mantém o navegador aberto por algum tempo para capturar as requisições WebSocket
        page.wait_for_timeout(10000)  # Espera 10 segundos (10000 ms)
        browser.close()



if __name__ == "__main__":
    capture_websocket_url()