# src/client/tls_wrapper.py
import socket
import ssl
import screen_share
import input_control
import threading

SERVER_IP = "192.168.25.61"
SERVER_PORT = 4433

def initiate_secure_connection():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('certificates/ca_bundle.pem')

    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(raw_sock, server_hostname=SERVER_IP)

    try:
        secure_sock.connect((SERVER_IP, SERVER_PORT))
        print("[INFO] TLS 연결 성공")

        threading.Thread(target=screen_share.start_screen_stream, args=(secure_sock,), daemon=True).start()
        threading.Thread(target=input_control.listen_for_input, args=(secure_sock,), daemon=True).start()

        while True:
            pass  # 연결 유지
    except Exception as e:
        print(f"[ERROR] TLS 연결 실패: {e}")
    finally:
        secure_sock.close()
