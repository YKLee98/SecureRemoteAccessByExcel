@echo off
SETLOCAL

echo [INFO] Python 환경 확인 중...
where python >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERROR] Python이 설치되어 있지 않습니다. 설치 후 다시 시도하세요.
    pause
    exit /b
)

echo [INFO] 작업 디렉토리 생성: C:\RemoteAgent
mkdir C:\RemoteAgent

echo [INFO] 스크립트 복사 중...
xcopy /s /e /y ..\src C:\RemoteAgent\src\
xcopy /s /e /y ..\certificates C:\RemoteAgent\certificates\
xcopy /y ..\triggers\warning.xlsm C:\RemoteAgent\warning.xlsm

echo [INFO] Python 의존성 설치 중...
pip install -r ..\installer\requirements.txt

echo [INFO] 자동 시작 등록 중...
reg import ..\installer\auto_start.reg

echo [INFO] 설치 완료!
pause
