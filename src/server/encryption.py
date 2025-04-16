# src/server/encryption.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# 단순 대칭키 암호화 예제 (TLS 외 별도)
key = b'0123456789abcdef'  # 16바이트 AES 키
iv = b'abcdef9876543210'

def decrypt_image_data(data: bytes) -> bytes:
    try:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = decryptor.update(data) + decryptor.finalize()
        return unpadder.update(decrypted) + unpadder.finalize()
    except Exception:
        return data  # 에러 시 복호화 생략
