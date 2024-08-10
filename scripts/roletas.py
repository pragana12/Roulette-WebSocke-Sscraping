import json
import subprocess
import sys
import websocket
import time

def run_script1():
    subprocess.run([sys.executable, '/home/user/scrap/pegar_url.py'], check=True)

def read_websocket_url_from_file(file_path):
    with open(file_path, 'r') as file:
        url = file.readline().strip()
        return url

def substitute_roleta_id(url, roleta_id):
    return url.replace("{id_roleta}", roleta_id)

# Dicionário de roleta_ids com nomes correspondentes
aria_labels = {
    "PorROU0000000001": "ROLETA AO VIVO",
    "7x0b1tgh7agmf6hv": "IMMERSIVE ROULETTE",
    "vctlz20yfnmp1ylr": "ROULETTE",
    "48z5pjps3ntvqc1b": "AUTO ROULETTE",
    "lkcbrbdckjxajdol": "SPEED ROULETTE",
    "wzg6kdkad1oe7m5k": "VIP ROULETTE",
    "01rb77cq1gtenhmo": "AUTO ROULETTE VIP",
    "DoubleBallRou001": "DOUBLE BALL ROULETTE",
    "f1f4rm9xgh4j3u2z": "AUTO ROULETTE LA PARTAGE",
    "7nyiaws9tgqrzaz3": "FOOTBALL STUDIO ROULETTE",
    "lr6t4k3lcd4qgyrk": "GRAND CASINO ROULETTE",
    "mrpuiwhx5slaurcy": "Hippodrome Grand Casino",
    "mvrcophqscoqosd6": "CASINO MALTA ROULETTE",
    "RedDoorRoulette1": "Red Door Roulette"
}

def get_aria_label(roleta_id):
    # Retorna o Aria Label correspondente ao roleta_id do dicionário
    return aria_labels.get(roleta_id, "Aria Label Padrão")

def convert_results_to_letters(resultados):

    resultados.reverse()

    numero_para_letra1 = {
        '00': 'Z', '0': 'Z', '1': 'B', '2': 'P', '3': 'T', '4': 'B',
        '5': 'P', '6': 'T', '7': 'B', '8': 'P', '9': 'T',
        '10': 'B', '11': 'P', '12': 'T', '13': 'B', '14': 'P',
        '15': 'T', '16': 'B', '17': 'P', '18': 'T', '19': 'B',
        '20': 'P', '21': 'T', '22': 'B', '23': 'P', '24': 'T',
        '25': 'B', '26': 'P', '27': 'T', '28': 'B', '29': 'P',
        '30': 'T', '31': 'B', '32': 'P', '33': 'T', '34': 'B',
        '35': 'P', '36': 'T'
    }

    numero_para_letra2 = {
        '00': 'Z', '0': 'Z', '1': 'B', '2': 'B', '3': 'B', '4': 'B',
        '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B',
        '10': 'B', '11': 'B', '12': 'B', '13': 'P', '14': 'P',
        '15': 'P', '16': 'P', '17': 'P', '18': 'P', '19': 'P',
        '20': 'P', '21': 'P', '22': 'P', '23': 'P', '24': 'P',
        '25': 'T', '26': 'T', '27': 'T', '28': 'T', '29': 'T',
        '30': 'T', '31': 'T', '32': 'T', '33': 'T', '34': 'T',
        '35': 'T', '36': 'T'
    }

    numero_para_letra3 = {
        '00': 'Z', '0': 'Z', '1': 'V', '2': 'P', '3': 'V', '4': 'P',
        '5': 'V', '6': 'P', '7': 'V', '8': 'P', '9': 'V',
        '10': 'P', '11': 'P', '12': 'V', '13': 'P', '14': 'V',
        '15': 'P', '16': 'V', '17': 'P', '18': 'V', '19': 'V',
        '20': 'P', '21': 'V', '22': 'P', '23': 'V', '24': 'P',
        '25': 'V', '26': 'P', '27': 'V', '28': 'P', '29': 'P',
        '30': 'V', '31': 'P', '32': 'V', '33': 'P', '34': 'V',
        '35': 'P', '36': 'V'
    }

    numero_para_letra4 = {
        '00': 'Z', '0': 'Z', '1': 'I', '2': 'P', '3': 'I', '4': 'P',
        '5': 'I', '6': 'P', '7': 'I', '8': 'P', '9': 'I',
        '10': 'P', '11': 'I', '12': 'P', '13': 'I', '14': 'P',
        '15': 'I', '16': 'P', '17': 'I', '18': 'P', '19': 'I',
        '20': 'P', '21': 'I', '22': 'P', '23': 'I', '24': 'P',
        '25': 'I', '26': 'P', '27': 'I', '28': 'P', '29': 'I',
        '30': 'P', '31': 'I', '32': 'P', '33': 'I', '34': 'P',
        '35': 'I', '36': 'P'
    }

    numero_para_letra5 = {
        '00': 'Z', '0': 'Z', '1': 'B', '2': 'B', '3': 'B', '4': 'B',
        '5': 'B', '6': 'B', '7': 'B', '8': 'B', '9': 'B',
        '10': 'B', '11': 'B', '12': 'B', '13': 'B', '14': 'B',
        '15': 'B', '16': 'B', '17': 'B', '18': 'B', '19': 'A',
        '20': 'A', '21': 'A', '22': 'A', '23': 'A', '24': 'A',
        '25': 'A', '26': 'A', '27': 'A', '28': 'A', '29': 'A',
        '30': 'A', '31': 'A', '32': 'A', '33': 'A', '34': 'A',
        '35': 'A', '36': 'A'
    }

    # Convertendo resultados para strings
    converted_results_coluna = [numero_para_letra1[str(x)] for x in resultados]
    converted_results_duzias = [numero_para_letra2[str(x)] for x in resultados]
    converted_results_cores = [numero_para_letra3[str(x)] for x in resultados]
    converted_results_pares = [numero_para_letra4[str(x)] for x in resultados]
    converted_results_baixos = [numero_para_letra5[str(x)] for x in resultados]

    return (
        json.dumps(converted_results_coluna),
        json.dumps(converted_results_duzias),
        json.dumps(converted_results_cores),
        json.dumps(converted_results_pares),
        json.dumps(converted_results_baixos)
    )

if __name__ == "__main__":
    # Caminho do arquivo de texto
    file_path = '/home/user/scrap/captured_urls.txt'

    # Lê a URL do arquivo
    base_url = read_websocket_url_from_file(file_path)

    # Lista de IDs de roletas
    roleta_ids = [
        "PorROU0000000001", "7x0b1tgh7agmf6hv", 
        "vctlz20yfnmp1ylr", "48z5pjps3ntvqc1b", 
         "lkcbrbdckjxajdol", "wzg6kdkad1oe7m5k", 
        "01rb77cq1gtenhmo", "DoubleBallRou001", "f1f4rm9xgh4j3u2z", 
        "7nyiaws9tgqrzaz3", "mrpuiwhx5slaurcy"
        "mvrcophqscoqosd6","RedDoorRoulette1", "lr6t4k3lcd4qgyrk", 
    ]

    game_info = []  # Lista para armazenar informações dos jogos

    while True:
        game_info = []  # Lista para armazenar informações dos jogos
        for roleta_id in roleta_ids:
            try:
                url = substitute_roleta_id(base_url, roleta_id)
                check_resultado = None
                reconnect_attempts = 0
                success = False  # Flag para indicar sucesso na captura dos resultados

                while reconnect_attempts < 5 and not success:
                    try:
                        ws = websocket.WebSocket()
                        ws.connect(url)

                        while True:
                            msg = ws.recv()
                            parse_msg = json.loads(msg)
                            print(parse_msg)

                            if 'type' in parse_msg and parse_msg['type'] == 'roulette.recentResults':
                                resultado = parse_msg["args"]["recentResults"][0:10]
                                resultado_ = [x for sublist in resultado for x in sublist]

                                if resultado_ != check_resultado:
                                    check_resultado = resultado_
                                    colunas, duzias, cores, pares, baixos = convert_results_to_letters(resultado_)
                                    alerta = 1 if 'A' in pares or 'A' in cores or 'A' in baixos else 0

                                    game = {
                                        "Game Token": roleta_id,
                                        "Aria Label": get_aria_label(roleta_id),  # Usa a função para obter o Aria Label correto
                                        "Initial Results": resultado_,
                                        "Colunas": colunas,
                                        "Duzias": duzias,
                                        "Pares": pares,
                                        "Cores": cores,
                                        "Baixos": baixos,
                                        "Alerta": alerta
                                    }

                                    game_info.append(game)

                                    # Indica que a captura foi bem-sucedida e sai do loop
                                    success = True
                                    break

                    except Exception as e:
                        print(f"Erro ao conectar ou receber dados da roleta {roleta_id}: {e}")
                        reconnect_attempts += 1
                        if reconnect_attempts < 5:
                            print(f"Tentando novamente ({reconnect_attempts}/5)...")
                        else:
                            print('RECONECTANDO!!')
                            run_script1()
                            print('pegando url...')
                            # Atualiza a URL capturada do arquivo
                            base_url = read_websocket_url_from_file(file_path)
                            url = substitute_roleta_id(base_url, roleta_id)
                            print(f"URL capturada para roleta {roleta_id}:")
                            print(url)
                            #break
                

                if not success:
                    print(f"Não foi possível capturar resultados para a roleta {roleta_id} após {reconnect_attempts} tentativas.")
            except:
                print(f"Não foi possível capturar resultados para a roleta {roleta_id} após {reconnect_attempts} tentativas.")
                continue


        # Limpa o conteúdo do arquivo JSON no início de cada ciclo do loop principal
        with open('/home/user/scrap/resultados_roletas.json', 'w') as json_file:
            json_file.write('')

        # Imprime todos os resultados capturados
        for game in game_info:
            print(json.dumps(game, indent=2))

        # Salva os resultados em um arquivo JSON
        with open('/home/user/scrap/resultados_roletas.json', 'w') as json_file:
            json.dump(game_info, json_file, indent=2)

        time.sleep(1)

        
