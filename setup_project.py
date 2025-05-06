import os
import pathlib

def create_file(path, content=""):
    """Create file with content if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {path}")
    else:
        print(f"Skipped: {path} (already exists)")

def setup_project():
    """Set up project structure for dont-starve-AIbot."""
    base_dir = os.getcwd()  # Current directory (dont-starve-AIbot)

    # scripts/
    create_file(os.path.join(base_dir, "scripts", "__init__.py"), "")
    create_file(os.path.join(base_dir, "scripts", "visual_parser.py"), """import cv2
import pytesseract
import numpy as np
from PIL import Image

def parse_state(screenshot_path):
    img = Image.open(screenshot_path)
    img_np = np.array(img)
    # Tree detection (green)
    hsv = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (30, 50, 50), (90, 255, 255))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    trees = [cv2.boundingRect(c) for c in contours]
    # Inventory (placeholder)
    inventory_text = pytesseract.image_to_string(img_np)
    state = {
        "time": "day" if "Day" in inventory_text else "night",
        "inventory": {"wood": 0},  # TODO: Parse
        "nearby": [{"type": "tree", "x": x, "y": y} for (x, y, w, h) in trees]
    }
    return state
""")
    create_file(os.path.join(base_dir, "scripts", "llm_decider.py"), """import requests

def decide_action(state, api_key, api_url="https://api.deepseek.com"):
    prompt = f"Game state: {state}. Suggest an action (e.g., chop tree, build campfire)."
    response = requests.post(api_url, json={"prompt": prompt}, headers={"Authorization": f"Bearer {api_key}"})
    action = response.json().get("action", {"action": "idle"})
    return action
""")
    create_file(os.path.join(base_dir, "scripts", "executor.py"), """import pyautogui
import time

def execute_action(action):
    if action["action"] == "chop_tree":
        x, y = action.get("target", {"x": 0, "y": 0}).values()
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(1)  # Simulate chopping
""")
    create_file(os.path.join(base_dir, "scripts", "replay_parser.py"), """import json

def parse_replay(json_path):
    with open(json_path) as f:
        replay = json.load(f)
    return replay  # TODO: Extract state-action pairs
""")
    create_file(os.path.join(base_dir, "scripts", "main.py"), """from visual_parser import parse_state
from llm_decider import decide_action
from executor import execute_action
import time

def main():
    while True:
        state = parse_state("data/screenshots/current.png")  # TODO: Dynamic screenshot
        action = decide_action(state, api_key="YOUR_API_KEY")
        execute_action(action)
        time.sleep(5)  # 5s loop

if __name__ == "__main__":
    main()
""")
    create_file(os.path.join(base_dir, "scripts", "config.py"), """CONFIG = {
    "api_key": "YOUR_API_KEY",
    "game_resolution": (1920, 1080),
    "window_position": (0, 0)
}
""")

    # mods/AIBotAgent/
    create_file(os.path.join(base_dir, "mods", "AIBotAgent", "modinfo.lua"), """name = "AIBot Agent"
description = "AI agent for Don't Starve Together"
author = "peter-zx"
version = "0.1"
forumthread = ""
api_version = 10
dst_compatible = true
all_clients_require_mod = true
""")
    create_file(os.path.join(base_dir, "mods", "AIBotAgent", "modmain.lua"), "-- TODO: Integrate Python (JSON output/actions)")

    # mods/AIBotRecorder/
    create_file(os.path.join(base_dir, "mods", "AIBotRecorder", "modinfo.lua"), """name = "AIBot Recorder"
description = "Records player actions for AI training"
author = "peter-zx"
version = "0.1"
forumthread = ""
api_version = 10
dst_compatible = true
all_clients_require_mod = true
""")
    create_file(os.path.join(base_dir, "mods", "AIBotRecorder", "modmain.lua"), """local json = GLOBAL.json
local function save_replay(state, action)
    local data = {timestamp = os.date(), state = state, action = action}
    local file = io.open("replays/replay.json", "a")
    file:write(json.encode(data) .. "\n")
    file:close()
end

AddPlayerPostInit(function(player)
    player:ListenForEvent("performaction", function(inst, data)
        local state = {
            time = GLOBAL.TheWorld.state.phase,
            inventory = player.components.inventory:GetItems(),
            nearby = GLOBAL.TheSim:FindEntities(player.Transform:GetWorldPosition(), 10)
        }
        local action = {type = data.action, target = data.target}
        save_replay(state, action)
    end)
end)
""")

    # data/
    create_file(os.path.join(base_dir, "data", "replays", "example.json"), """{
    "timestamp": "2025-05-03T12:48:00",
    "state": {"time": "day", "inventory": {"wood": 10}, "nearby": ["tree"]},
    "action": {"type": "chop_tree", "target": {"x": 110, "y": 210}}
}
""")
    os.makedirs(os.path.join(base_dir, "data", "screenshots"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "data", "recordings"), exist_ok=True)

    # docs/
    create_file(os.path.join(base_dir, "docs", "README.md"), """# Don't Starve AI Bot
AI agent for DST with growth attributes. Includes Agent Mod (controls character) and Recorder Mod (collects player data).

## Setup
- Install Python dependencies: `pip install -r requirements.txt`
- Configure `config.py` (API key, game settings).
- Install mods in DST: copy `mods/AIBotAgent` and `mods/AIBotRecorder` to DST mod folder.

## Run
```bash
python scripts/main.py
```
""")
    create_file(os.path.join(base_dir, "docs", "setup.md"), """# Setup
## Python
- Python 3.8+
- `pip install -r requirements.txt`
## DST Mods
- Copy `mods/AIBotAgent` and `mods/AIBotRecorder` to `C:\\Program Files (x86)\\Steam\\steamapps\\common\\Don't Starve Together\\mods`.
- Enable mods in DST.
## Tools
- OBS: Record gameplay.
""")

    # requirements.txt
    create_file(os.path.join(base_dir, "requirements.txt"), """opencv-python
pytesseract
pyautogui
pynput
requests
pillow
numpy
""")

if __name__ == "__main__":
    setup_project()