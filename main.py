import pyautogui
import pyperclip
import subprocess

subprocess.call("C:\Program Files (x86)\ICETalk\Launcher.exe")
target = pyautogui.getActiveWindow()

while True:
    windows = pyautogui.getAllWindows()

    for window in windows:
        if window.title == "쪽지 전송":
            target = window
    if target.title == "쪽지 전송":
        break

if target.isActive == False:
    target.activate()

pyperclip.copy('카트에 담을 크기의 택배가 왔습니다. 행정실에서 찾아가주세요:)')
pyautogui.click(target.left+40, target.top+300, duration = 0.1)

pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('alt')
pyautogui.press('enter')
pyautogui.keyUp('alt')
pyautogui.press('enter')

ICETalk = pyautogui.getWindowsWithTitle("ICETalk")[0]
ICETalk.close()