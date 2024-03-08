import time
import pyautogui

pyautogui.FAILSAFE = False  # FailSafeException을 방지합니다.

screenWidth, screenHeight = pyautogui.size()  # 화면 크기를 가져옵니다.
centerX = screenWidth / 2
centerY = screenHeight / 2

while True:
    # 마우스를 화면 중앙으로 이동하고 클릭합니다.
    pyautogui.moveTo(centerX, centerY)
    pyautogui.click()

    time.sleep(60)  # 1분마다 마우스를 움직입니다. 필요에 따라 시간을 조정하세요.
