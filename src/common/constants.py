# src/common/constants.py

# 서버 정보
SERVER_IP = "192.168.25.61"
SERVER_PORT = 4433

# 인증 토큰
AUTH_TOKEN = "secure_token_2025"

# TLS 인증서 경로
CERTIFICATE_PATHS = {
    "client_ca_bundle": "certificates/ca_bundle.pem",
    "server_cert": "certificates/server.crt",
    "server_key": "certificates/server.key"
}

# AES 암호화 설정
AES_KEY = b"0123456789abcdef"    # 16 bytes
AES_IV = b"abcdef9876543210"     # 16 bytes

# 스크린샷 저장 디렉토리
SCREENSHOT_SAVE_DIR = "screenshots"

# 로그 디렉토리
LOG_DIR = "logs"

# 명령어 종류
COMMAND_TYPES = {
    "MOVE": "마우스 이동",
    "CLICK": "클릭",
    "TYPE": "텍스트 입력"
}
