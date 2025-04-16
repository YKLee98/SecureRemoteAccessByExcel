# src/server/session_manager.py
import threading

sessions = {}
lock = threading.Lock()

def register_session(addr, conn):
    with lock:
        sessions[addr] = conn
        print(f"[INFO] 세션 등록: {addr}")

def unregister_session(addr):
    with lock:
        if addr in sessions:
            del sessions[addr]
            print(f"[INFO] 세션 해제: {addr}")

def get_active_sessions():
    with lock:
        return list(sessions.keys())
