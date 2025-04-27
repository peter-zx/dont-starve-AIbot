import pyautogui
import time
import math
import cv2
import numpy as np
from PIL import Image

def move_circle(circles=6, step_duration=0.1, radius=1.0):
    """让角色画圆，循环指定圈数，接近圆形轨迹"""
    print(f"开始画圆，转 {circles} 圈...")
    steps_per_circle = 36
    total_steps = int(circles * steps_per_circle)
    
    for step in range(total_steps):
        theta = (2 * math.pi * step) / steps_per_circle
        x_speed = math.cos(theta) * radius
        y_speed = math.sin(theta) * radius
        
        if x_speed > 0:
            pyautogui.keyDown('d')
            time.sleep(step_duration * abs(x_speed))
            pyautogui.keyUp('d')
        elif x_speed < 0:
            pyautogui.keyDown('a')
            time.sleep(step_duration * abs(x_speed))
            pyautogui.keyUp('a')
            
        if y_speed > 0:
            pyautogui.keyDown('w')
            time.sleep(step_duration * abs(y_speed))
            pyautogui.keyUp('w')
        elif y_speed < 0:
            pyautogui.keyDown('s')
            time.sleep(step_duration * abs(y_speed))
            pyautogui.keyUp('s')
            
        time.sleep(0.05)
    
    print("画圆完成！")

def take_screenshot(window, save_path="screenshot.png"):
    """截取游戏窗口的截图并保存"""
    x, y = window.left, window.top
    width, height = window.width, window.height
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(save_path)
    print(f"截图已保存到 {save_path}")
    return save_path

def click_at_position(x, y):
    """在指定坐标点击"""
    pyautogui.click(x, y)
    time.sleep(1)

def gather_resource(window, grok_instructions):
    """根据Grok的指令采集资源（比如草）"""
    print("开始采集资源...")
    # 假设Grok返回坐标
    if "click_x" in grok_instructions and "click_y" in grok_instructions:
        click_x = window.left + grok_instructions["click_x"]
        click_y = window.top + grok_instructions["click_y"]
        click_at_position(click_x, click_y)
        print(f"点击采集：({click_x}, {click_y})")
    else:
        print("Grok未提供有效坐标，跳过采集")

def build_science_machine(window, grok_instructions):
    """根据Grok的指令建造科学机器"""
    print("开始建造科学机器...")
    # 确保窗口焦点
    x, y = window.left, window.top
    pyautogui.click(x + 50, y + 50)
    time.sleep(1)
    
    # 点击科学机器图标
    if "science_machine_x" in grok_instructions and "science_machine_y" in grok_instructions:
        sm_x = window.left + grok_instructions["science_machine_x"]
        sm_y = window.top + grok_instructions["science_machine_y"]
        click_at_position(sm_x, sm_y)
        print(f"点击科学机器图标：({sm_x}, {sm_y})")
    else:
        print("Grok未提供科学机器坐标，跳过")
        return
    
    # 点击放置按钮
    if "place_button_x" in grok_instructions and "place_button_y" in grok_instructions:
        pb_x = window.left + grok_instructions["place_button_x"]
        pb_y = window.top + grok_instructions["place_button_y"]
        click_at_position(pb_x, pb_y)
        print(f"点击放置按钮：({pb_x}, {pb_y})")
    else:
        print("Grok未提供放置按钮坐标，跳过")