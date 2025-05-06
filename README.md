Dont Starve AI Bot

项目目标

开发一个 AI 机器人，控制电脑玩《饥荒联机版》（Don't Starve Together），通过脚本启动器调用大语言模型（如 Grok）作为大脑，实现自动化操作（如移动、采集、建造）。

项目介绍

这是一个针对《饥荒联机版》的自动化脚本项目，基于 Python 和 PyAutoGUI。当前功能包括：

'''
dont-starve-AIbot/
├── scripts/                    # Python 脚本（智能体逻辑）
│   ├── __init__.py
│   ├── visual_parser.py        # OpenCV/pytesseract 状态解析
│   ├── llm_decider.py          # LLM 决策
│   ├── executor.py             # pyautogui 动作
│   ├── replay_parser.py        # 解析辅助 mod JSON
│   ├── main.py                 # 主程序
│   └── config.py               # 配置
├── mods/                       # DST mod
│   ├── AIBotAgent/             # 智能体 mod（占位）
│   │   ├── modinfo.lua
│   │   └── modmain.lua
│   ├── AIBotRecorder/          # 辅助 mod（数据收集）
│   │   ├── modinfo.lua
│   │   └── modmain.lua
├── data/                       # 数据存储
│   ├── replays/                # 辅助 mod JSON
│   │   └── example.json
│   ├── screenshots/            # 截图
│   └── recordings/             # 录屏
├── docs/                       # 文档
│   ├── README.md               # 项目说明
│   └── setup.md                # 环境配置
├── requirements.txt            # Python 依赖
└── .gitignore                  # Git 忽略（已有）
'''




自动移动（画圆轨迹）



截图并接入大语言模型分析（准备实现采集和建造）

'''

项目结构：

dont-starve-AIbot/
├── src/
│   ├── __init__.py
│   ├── window_utils.py
│   ├── game_control.py
│   └── app.py
├── venv/
├── main.py
├── move_dst_window.py
└── requirements.txt

'''

使用方式





环境准备：





安装 Python 3.10 或 3.11。



克隆仓库：

git clone https://github.com/peter-zx/dont-starve-AIbot.git
cd dont-starve-AIbot



创建并激活虚拟环境：

python -m venv venv
.\venv\Scripts\activate  # Windows



安装依赖：

pip install -r requirements.txt



游戏准备：





启动《饥荒联机版》，设置窗口模式（建议 1296x759）。



进入游戏世界（建议上帝模式），确保输入法为英文，屏幕缩放 100%。



运行脚本：





在项目根目录运行：

python main.py



脚本会在 15 秒后开始，需确保游戏窗口在前台。



当前功能：





自动截图并保存为 screenshot.png。



模拟接入大语言模型，执行采集和建造（需提供截图给模型）。



调试：





截图位置：dont-starve-AIbot/screenshot.png。



坐标不准：调整 src/app.py 中的 grok_instructions。