@echo off
echo [INFO] 원격 에이전트 제거 중...
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v RemoteAgent /f
rmdir /s /q C:\RemoteAgent
echo [INFO] 제거 완료
pause
