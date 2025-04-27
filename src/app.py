import pyautogui
import time
from src.window_utils import get_game_window, activate_window
from src.game_control import take_screenshot, move_forward, build_item

# 防止失控：鼠标移到左上角停止脚本
pyautogui.FAILSAFE = True

def main():
    """主函数，协调窗口检测和游戏控制"""
    print("15秒后开始，请手动进入饥荒联机版游戏世界，确保游戏窗口在前台，输入法为英文！")
    time.sleep(15)
    
    # 找窗口
    window = get_game_window(title="Don't Starve Together")
    
    # 激活窗口
    activate_window(window)
    
    # 1. 向前移动一段距离
    move_forward(duration=3)
    
    # 2. 截图并建造斧头（工具）
    print("截图以建造斧头...")
    screenshot_path = take_screenshot(window)
    print("请将 screenshot.png 提供给Grok，获取斧头和放置按钮坐标后输入...")
    build_item(window, "斧头")
    
    # 3. 截图并建造科学机器（建筑）
    print("截图以建造科学机器...")
    screenshot_path = take_screenshot(window)
    print("请将 screenshot.png 提供给Grok，获取科学机器和放置按钮坐标后输入...")
    build_item(window, "科学机器")

if __name__ == "__main__":
    main()