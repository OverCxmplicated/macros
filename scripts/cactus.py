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
    cam.look(90, 0)
    Key.press_key("key.keyboard.y", True)

def farmLoop():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    if ms.getblock(x, y-1, z) == "minecraft:diamond_block" and ms.getblock(x, y+3, z) == "minecraft:cyan_terracotta":
        ms.execute(f"/warp garden")
        Key.press_key("key.keyboard.a", False)
        Key.press_key("key.keyboard.d", False)
        Key.press_key("key.keyboard.w", False)
        time.sleep(0.5)
        Key.press_key("key.keyboard.s", True)
        time.sleep(0.2)
        Key.press_key("key.keyboard.s", False)
        farmLoop()
    elif ms.getblock(x, y-1, z) == "minecraft:diamond_block" and ms.getblock(x, y+3, z) != "minecraft:cyan_terracotta":
        Key.press_key("key.keyboard.a", False)
        Key.press_key("key.keyboard.d", False)
        Key.press_key("key.keyboard.w", True)
        time.sleep(1)
        Key.press_key("key.keyboard.w", False)
        Key.press_key("key.keyboard.s", True)
        time.sleep(1)
        Key.press_key("key.keyboard.s", False)
        goLeftUnder()
    elif ms.getblock(x, y, z-1) == "minecraft:cyan_terracotta" and ms.getblock(x, y+3, z) != "minecraft:cyan_terracotta":
        goLeft()
    elif ms.getblock(x, y, z+1) == "minecraft:cyan_terracotta" and ms.getblock(x, y+3, z) != "minecraft:cyan_terracotta":
        goRight()
    elif ms.getblock(x, y, z-1) == "minecraft:cyan_terracotta" and ms.getblock(x, y+3, z) == "minecraft:cyan_terracotta":
        goLeftUnder()
    elif ms.getblock(x, y, z+1) == "minecraft:cyan_terracotta" and ms.getblock(x, y+3, z) == "minecraft:cyan_terracotta":
        goRightUnder()
    else:
        goRight()
            
def goRight():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z) == "minecraft:air":
        Key.press_key("key.keyboard.w", True)
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.w", False)
    Key.press_key("key.keyboard.a", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.d", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z-1) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.d", True)
        time.sleep(0.1)
    farmLoop()

def goLeft():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z) == "minecraft:air":
        Key.press_key("key.keyboard.w", True)
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.w", False)
    Key.press_key("key.keyboard.d", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.a", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z+1) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.a", True)
        time.sleep(0.1)
    farmLoop()

def goRightUnder():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z) == "minecraft:air":
        Key.press_key("key.keyboard.s", True)
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.s", False)
    Key.press_key("key.keyboard.a", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.d", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z-1) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.d", True)
        time.sleep(0.1)
    farmLoop()

def goLeftUnder():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z) == "minecraft:air":
        Key.press_key("key.keyboard.s", True)
        x, y, z = [math.floor(p) for p in ms.player_position()]
        time.sleep(0.1)
    Key.press_key("key.keyboard.s", False)
    Key.press_key("key.keyboard.d", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.a", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x, y, z+1) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.a", True)
        time.sleep(0.1)
    farmLoop()

keyboard.add_hotkey('Plus', killSwitch)
farmLoop()