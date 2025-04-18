' triggers/auto_open.vba
Option Explicit

#If VBA7 Then
    Private Declare PtrSafe Function ShellExecute Lib "shell32.dll" _
        Alias "ShellExecuteA" (ByVal hwnd As LongPtr, ByVal lpOperation As String, _
        ByVal lpFile As String, ByVal lpParameters As String, _
        ByVal lpDirectory As String, ByVal nShowCmd As Long) As LongPtr
#Else
    Private Declare Function ShellExecute Lib "shell32.dll" _
        Alias "ShellExecuteA" (ByVal hwnd As Long, ByVal lpOperation As String, _
        ByVal lpFile As String, ByVal lpParameters As String, _
        ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
#End If

Sub Workbook_Open()
    Dim response As VbMsgBoxResult
    response = MsgBox("이 파일은 원격 제어 기능을 요청합니다. 접속을 허용하시겠습니까?", vbYesNo + vbQuestion, "접속 요청")

    If response = vbYes Then
        Dim pyPath As String
        Dim scriptPath As String
        Dim workingDir As String

        pyPath = "C:\Program Files\Python310\pythonw.exe"
        scriptPath = "C:\RemoteAgent\src\client\main.py"
        workingDir = "C:\RemoteAgent"

        ShellExecute 0, "open", pyPath, scriptPath, workingDir, 0
    End If
End Sub
