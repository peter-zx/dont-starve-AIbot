import pyautogui
import time
import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import simpledialog

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

def get_user_input(prompt):
    """弹窗输入坐标"""
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("输入", prompt, parent=root)
    root.destroy()
    try:
        return tuple(map(int, user_input.split(',')))
    except (ValueError, AttributeError):
        print("输入格式错误，请输入 x,y（如 300,400）")
        return None

def move_forward(duration=3):
    """向前移动指定时间"""
    print(f"向前移动 {duration} 秒...")
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')
    print("移动完成！")

def build_item(window, item_name):
    """建造指定物品（工具或建筑）：弹出输入窗口，获取Grok提供的坐标"""
    print(f"开始建造 {item_name}...")
    x, y = window.left, window.top
    pyautogui.click(x + 50, y + 50)
    time.sleep(1)
    
    # 获取物品图标坐标
    prompt = f"请提供Grok给的 {item_name} 坐标（x,y，如 130,130）："
    item_coords = get_user_input(prompt)
    if item_coords:
        item_x, item_y = item_coords
        item_x += window.left
        item_y += window.top
        click_at_position(item_x, item_y)
        print(f"点击 {item_name} 图标：({item_x}, {item_y})")
    else:
        print(f"未提供 {item_name} 坐标，跳过")
        return
    
    # 获取放置按钮坐标
    prompt = "请提供Grok给的放置按钮坐标（x,y，如 648,689）："
    pb_coords = get_user_input(prompt)
    if pb_coords:
        pb_x, pb_y = pb_coords
        pb_x += window.left
        pb_y += window.top
        click_at_position(pb_x, pb_y)
        print(f"点击放置按钮：({pb_x}, {pb_y})")
    else:
        print("未提供放置按钮坐标，跳过")