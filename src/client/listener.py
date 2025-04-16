# src/client/listener.py
import psutil

def is_excel_opened(file_name: str) -> bool:
    """
    엑셀 프로세스를 스캔하고 특정 파일이 열려 있는지 확인
    """
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'EXCEL.EXE' in proc.info['name']:
                cmdline = ' '.join(proc.info.get('cmdline', []))
                if file_name.lower() in cmdline.lower():
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False
