# src/server/authentication.py
from logger import log_event

def authenticate(conn) -> bool:
    """
    간단한 인증 토큰 방식 (확장 가능)
    """
    try:
        conn.send(b"AUTH_TOKEN:")
        token = conn.recv(1024).decode('utf-8').strip()
        if token == "secure_token_2025":
            return True
        return False
    except Exception as e:
        log_event("AUTH", f"인증 오류: {e}")
        return False
