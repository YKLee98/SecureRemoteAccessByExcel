# src/server/main.py
import socket
import ssl
import threading
from connection_handler import handle_client
from logger import init_logger

HOST = '0.0.0.0'
PORT = 4433
CERT_FILE = 'certificates/server.crt'
KEY_FILE = 'certificates/server.key'
CA_FILE = 'certificates/ca_bundle.pem'

def start_server():
    init_logger()
    print("[INFO] 서버 시작 중...")

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.load_verify_locations(cafile=CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"[INFO] TLS 서버가 {HOST}:{PORT} 에서 대기 중...")

        with context.wrap_socket(sock, server_side=True) as ssock:
            while True:
                try:
                    client_conn, client_addr = ssock.accept()
                    print(f"[INFO] 클라이언트 연결: {client_addr}")
                    threading.Thread(target=handle_client, args=(client_conn, client_addr), daemon=True).start()
                except Exception as e:
                    print(f"[ERROR] 연결 처리 중 오류: {e}")

if __name__ == "__main__":
    start_server()
