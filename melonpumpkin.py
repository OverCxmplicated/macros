import minescript as ms
import time
from minescript_plus import Key
import sys
import keyboard
import math
import camera as cam


def killSwitch():
    Key.press_key("key.keyboard.w", False)
    Key.press_key("key.keyboard.a", False)
    Key.press_key("key.keyboard.s", False)
    Key.press_key("key.keyboard.d", False)
    Key.press_key("key.keyboard.y", False)
    ms.execute(r"\killjob -1")

def setOrientation():
    cam.look(0, -58.5)
    Key.press_key("key.keyboard.w", True)
    Key.press_key("key.keyboard.y", True)

def farmLoop():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    if ms.getblock(x, y-1, z) == "minecraft:diamond_block":
        ms.execute(f"/warp garden")
        Key.press_key("key.keyboard.a", False)
        Key.press_key("key.keyboard.d", False)
        Key.press_key("key.keyboard.w", False)
        time.sleep(0.5)
        Key.press_key("key.keyboard.s", True)
        time.sleep(0.2)
        Key.press_key("key.keyboard.s", False)
        farmLoop()
    elif ms.getblock(x-1, y+1, z) == "minecraft:dirt":
        goLeft()
    elif ms.getblock(x+1, y+1, z) == "minecraft:dirt":
        goRight()
    else:
        goRight()
            
def goRight():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    Key.press_key("key.keyboard.w", True)
    while ms.getblock(x, y+1, z+1) == "minecraft:air":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.a", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.d", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x-1, y+1, z) != "minecraft:dirt":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.d", True)
        time.sleep(0.1)
    farmLoop()

def goLeft():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    Key.press_key("key.keyboard.w", True)
    while ms.getblock(x, y+1, z+1) == "minecraft:air":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.d", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.a", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x+1, y+1, z) != "minecraft:dirt":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.a", True)
        time.sleep(0.1)
    farmLoop()

keyboard.add_hotkey('Plus', killSwitch)
farmLoop()