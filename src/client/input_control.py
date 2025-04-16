# src/client/input_control.py
import pyautogui
import socket
import struct

def listen_for_input(sock: socket.socket):
    """
    서버로부터 마우스 및 키보드 제어 명령을 수신하고 실행
    """
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            command = data.decode('utf-8')
            handle_input_command(command)
    except Exception as e:
        print(f"[ERROR] 입력 제어 수신 오류: {e}")

def handle_input_command(command: str):
    try:
        if command.startswith("MOVE"):
            _, x, y = command.split()
            pyautogui.moveTo(int(x), int(y))
        elif command.startswith("CLICK"):
            pyautogui.click()
        elif command.startswith("TYPE"):
            _, text = command.split(" ", 1)
            pyautogui.typewrite(text)
    except Exception as e:
        print(f"[ERROR] 입력 처리 오류: {e}")
