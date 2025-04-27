import pyautogui
import time
from src.window_utils import get_game_window, activate_window
from src.game_control import take_screenshot, gather_resource, build_science_machine

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
    
    # 1. 截图并让Grok分析（采集草）
    print("截图以进行采集...")
    screenshot_path = take_screenshot(window)
    # 模拟调用Grok（实际由用户提供截图，Grok返回坐标）
    grok_instructions_gather = {
        "click_x": 300,  # 假设Grok识别到草的坐标（相对窗口）
        "click_y": 400
    }
    gather_resource(window, grok_instructions_gather)
    
    # 2. 截图并让Grok分析（建造科学机器）
    print("截图以进行建造...")
    screenshot_path = take_screenshot(window)
    # 模拟调用Grok（实际由用户提供截图，Grok返回坐标）
    grok_instructions_build = {
        "science_machine_x": 130,
        "science_machine_y": 130,
        "place_button_x": window.width // 2,
        "place_button_y": window.height - 70
    }
    build_science_machine(window, grok_instructions_build)

if __name__ == "__main__":
    main()