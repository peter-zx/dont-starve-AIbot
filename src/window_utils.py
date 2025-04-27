import pygetwindow as gw
import pyautogui
import time

def get_game_window(title="Don't Starve Together"):
    """找到指定标题的游戏窗口，返回窗口对象"""
    windows = gw.getWindowsWithTitle(title)
    if not windows:
        print(f"错误：没找到 '{title}' 窗口！请确保游戏已打开并在窗口模式。")
        exit()
    window = windows[0]
    x, y = window.left, window.top
    width, height = window.width, window.height
    print(f"找到窗口！位置: ({x}, {y}), 尺寸: {width}x{height}")
    return window

def activate_window(window):
    """激活游戏窗口，确保焦点"""
    x, y = window.left, window.top
    print("激活游戏窗口...")
    pyautogui.click(x + 50, y + 50)  # 点击左上角（偏移50像素，避开边框）
    time.sleep(1)
    pyautogui.click(x + 50, y + 50)  # 再点一次，确保焦点
    time.sleep(1)