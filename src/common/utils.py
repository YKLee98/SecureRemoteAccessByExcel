# src/common/utils.py
import os
from datetime import datetime

def ensure_dir_exists(path: str):
    """
    디렉토리가 없으면 생성
    """
    if not os.path.exists(path):
        os.makedirs(path)

def get_timestamped_filename(prefix: str, ext: str = "log") -> str:
    """
    현재 날짜와 시간을 기준으로 고유한 파일 이름 생성
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{ext}"

def is_windows() -> bool:
    return os.name == 'nt'

def format_bytes(num_bytes: int) -> str:
    """
    바이트 수를 사람이 읽기 쉬운 형태로 변환
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.2f} TB"
