import pyautogui
import pygetwindow as gw
import time

# 防止失控：鼠标移到左上角停止脚本
pyautogui.FAILSAFE = True

def get_game_window():
    """找到饥荒联机版窗口，返回窗口对象"""
    windows = gw.getWindowsWithTitle("Don't Starve Together")
    if not windows:
        print("错误：没找到饥荒联机版窗口！请确保游戏已打开并在窗口模式。")
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
    pyautogui.click(x + 50, y + 50)  # 点击左上角（偏移50像素）
    time.sleep(1)
    pyautogui.click(x + 50, y + 50)  # 再点一次
    time.sleep(1)

def move_circle(circles=6, step_duration=0.5):
    """让角色画圆，循环指定圈数"""
    print(f"开始画圆，转 {circles} 圈...")
    directions = ['w', 'd', 's', 'a']  # WASD顺序，近似圆形
    for _ in range(circles):
        for direction in directions:
            pyautogui.keyDown(direction)
            time.sleep(step_duration)  # 每方向0.5秒
            pyautogui.keyUp(direction)
            time.sleep(0.1)  # 短暂暂停，防惯性
    print("画圆完成！")

def main():
    """主函数，协调窗口检测和移动"""
    print("15秒后开始，请手动进入饥荒联机版游戏世界，确保游戏窗口在前台，输入法为英文！")
    time.sleep(15)
    
    window = get_game_window()
    activate_window(window)
    move_circle(circles=6)

if __name__ == "__main__":
    main()