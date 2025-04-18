# screenshots/manager.py
import pyautogui
import os
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from common.constants import AES_KEY, AES_IV
import base64

ENC_DIR = os.path.join(os.path.dirname(__file__), "encrypted")
os.makedirs(ENC_DIR, exist_ok=True)

def capture_and_encrypt():
    # 스크린 캡처
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = os.path.join(ENC_DIR, f"{timestamp}.png")
    enc_path = os.path.join(ENC_DIR, f"{timestamp}.enc")

    # 원본 저장 (잠시 후 삭제)
    screenshot.save(raw_path)

    # 파일 읽고 암호화
    with open(raw_path, "rb") as f:
        data = f.read()

    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV))
    encryptor = cipher.encryptor()

    # 패딩
    pad = 16 - (len(data) % 16)
    data += bytes([pad] * pad)

    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(enc_path, "wb") as f:
        f.write(base64.b64encode(encrypted_data))

    os.remove(raw_path)  # 원본 삭제
    return enc_path
