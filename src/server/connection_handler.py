# src/server/connection_handler.py
from session_manager import register_session, unregister_session
from authentication import authenticate
from encryption import decrypt_image_data
from logger import log_event
import threading

def handle_client(conn, addr):
    if not authenticate(conn):
        conn.close()
        log_event(addr, "인증 실패")
        return

    register_session(addr, conn)
    log_event(addr, "세션 등록 완료")

    try:
        threading.Thread(target=receive_screen, args=(conn, addr), daemon=True).start()
        send_input_commands(conn)
    except Exception as e:
        log_event(addr, f"핸들러 오류: {e}")
    finally:
        unregister_session(addr)
        conn.close()
        log_event(addr, "세션 종료")

def receive_screen(conn, addr):
    try:
        while True:
            length_bytes = conn.recv(4)
            if not length_bytes:
                break
            length = int.from_bytes(length_bytes, 'big')
            image_data = b''
            while len(image_data) < length:
                chunk = conn.recv(length - len(image_data))
                if not chunk:
                    break
                image_data += chunk
            img = decrypt_image_data(image_data)
            # 저장하거나 스트림으로 처리 가능
            with open(f"screenshots/{addr[0]}.jpg", "wb") as f:
                f.write(img)
    except Exception as e:
        log_event(addr, f"화면 수신 오류: {e}")

def send_input_commands(conn):
    try:
        while True:
            cmd = input("입력 명령 (MOVE x y / CLICK / TYPE text): ")
            conn.sendall(cmd.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] 입력 전송 오류: {e}")
