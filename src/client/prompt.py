# src/client/prompt.py
import tkinter as tk
from tkinter import messagebox

def ask_user_permission() -> bool:
    """
    사용자에게 접속 허가 여부를 묻는 팝업 표시
    """
    root = tk.Tk()
    root.withdraw()  # 창 숨기기
    response = messagebox.askyesno("접속 요청", "이 컴퓨터에 원격 접속을 허용하시겠습니까?")
    root.destroy()
    return response
