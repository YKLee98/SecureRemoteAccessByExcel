# src/client/watchdog.py
import os
import ctypes

def verify_environment():
    """
    관리자 권한, 윈도우, 필수 라이브러리 점검
    """
    if os.name != 'nt':
        raise EnvironmentError("이 프로그램은 Windows에서만 실행됩니다.")
    
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            raise PermissionError("관리자 권한이 필요합니다.")
    except:
        raise PermissionError("관리자 권한 확인 실패")

    try:
        import pyautogui
        import psutil
    except ImportError as e:
        raise ImportError(f"필수 라이브러리 누락: {e}")
