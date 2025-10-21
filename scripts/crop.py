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
    cam.look(180, 0)
    Key.press_key("key.keyboard.y", True)

def farmLoop():
    x, y, z = [math.floor(p) for p in ms.player_position()]
    if ms.getblock(x-1, y, z) == "minecraft:cyan_terracotta":
        goRight()
    elif ms.getblock(x+1, y, z) == "minecraft:cyan_terracotta":
        goLeft()
    else:
        goLeft()
            
def goRight():
    time.sleep(0.1)
    Key.press_key("key.keyboard.a", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.d", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x+1, y, z) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.d", True)
        time.sleep(0.1)
    farmLoop()

def goLeft():
    time.sleep(0.1)
    Key.press_key("key.keyboard.d", False)
    Key.press_key("key.keyboard.y", True)
    Key.press_key("key.keyboard.a", True)
    time.sleep(0.1)
    x, y, z = [math.floor(p) for p in ms.player_position()]
    while ms.getblock(x-1, y, z) != "minecraft:cyan_terracotta":
        x, y, z = [math.floor(p) for p in ms.player_position()]
        setOrientation()
        Key.press_key("key.keyboard.a", True)
        time.sleep(0.1)
    farmLoop()

keyboard.add_hotkey('Plus', killSwitch)
farmLoop()