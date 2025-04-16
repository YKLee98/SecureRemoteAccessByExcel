# src/client/screen_share.py
import pyautogui
import socket
import time
import io
from PIL import Image

def capture_screen() -> bytes:
    """
    현재 화면을 캡처하고 JPEG로 인코딩한 후 바이트 배열로 반환
    """
    screenshot = pyautogui.screenshot()
    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='JPEG', quality=70)
    return img_byte_arr.getvalue()

def start_screen_stream(sock: socket.socket):
    """
    서버에 화면을 지속적으로 전송
    """
    try:
        while True:
            img_data = capture_screen()
            length = len(img_data).to_bytes(4, 'big')
            sock.sendall(length + img_data)
            time.sleep(0.1)  # 10 FPS 정도
    except Exception as e:
        print(f"[ERROR] 화면 전송 오류: {e}")
