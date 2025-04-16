# src/client/main.py
import listener
import watchdog
import prompt
import tls_wrapper

def start():
    watchdog.verify_environment()
    print("[INFO] 환경 점검 완료")

    if listener.is_excel_opened("warning.xlsx"):
        print("[INFO] warning.xlsx 파일이 열림")
        allowed = prompt.ask_user_permission()
        if allowed:
            print("[INFO] 사용자 접속 허가됨")
            tls_wrapper.initiate_secure_connection()
        else:
            print("[INFO] 사용자 접속 거부")

if __name__ == "__main__":
    start()
