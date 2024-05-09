import ctypes
import time

# Windows API 함수 가져오기
user32 = ctypes.windll.user32

# 화면 크기 가져오기
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
centerX = screenWidth // 2
centerY = screenHeight // 2

# 마우스 이동 및 클릭 함수 정의
def move_and_click(x, y):
    user32.SetCursorPos(x, y)
    user32.mouse_event(2, 0, 0, 0, 0)  # 왼쪽 버튼 클릭
    user32.mouse_event(4, 0, 0, 0, 0)  # 왼쪽 버튼 뗌

# 주기적으로 마우스 이동 및 클릭
while True:
    move_and_click(centerX, centerY)
    time.sleep(60)
