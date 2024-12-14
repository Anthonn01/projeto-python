import socket
import logging
import threading

# Configuração de logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para lidar com a conexão
def handle_client(client_socket, client_address):
    logging.info(f"Conexão estabelecida de {client_address}")
    try:
        client_socket.send(b"Bem-vindo ao honeypot!\n")
        while True:
            # Recebe dados do cliente
            data = client_socket.recv(1024)
            if not data:
                break
            logging.info(f"Dados recebidos de {client_address}: {data.decode()}")
            client_socket.send(b"Você está em um honeypot!\n")
    except Exception as e:
        logging.error(f"Erro ao lidar com o cliente {client_address}: {str(e)}")
    finally:
        logging.info(f"Conexão encerrada com {client_address}")
        client_socket.close()

# Função principal do honeypot
def start_honeypot(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    logging.info(f"Honeypot ativo e ouvindo em {host}:{port}")

    while True:
        # Aceita novas conexões
        client_socket, client_address = server.accept()
        logging.info(f"Nova conexão de {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

# Definindo o IP e porta do honeypot
host = "0.0.0.0"  # Aceitar conexões de qualquer IP
port = 9999        # Porta padrão para o honeypot

if __name__ == "__main__":
    start_honeypot(host, port)
