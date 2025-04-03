import os
import sys
import pyautogui as pg
import pymsgbox as pmb

from rich import inspect

# 定义常用位置
PCENTER = ['center', (0,0)]
PLEFT = ['left', (5,0)]
PRIGHT = ['right', (-5,0)]
PTOP = ['top', (0,5)]
PBOTTOM = ['bottom', (0,-5)]

# 一些配置

# 警告框超时时间，1000ms
ALERT_TIMEOUT = 1000
MOVETIMES = 5
PIC_CONFIDENCE = 0.95

def exists_image(image_path, timeout=5.0):
    try:
        pg.locateOnScreen(image_path, minSearchTime=timeout, confidence=PIC_CONFIDENCE)
        return True
    except:
        return False

def moveTo_image(image_path, position=PCENTER, duration=0.0, wait_time=0.3, timeout=5.0):
    pg.sleep(wait_time)
    error_message = ""
    
    try:
        error_message = "未找到 " + image_path.split("\\")[-1]
        locat = pg.locateOnScreen(image_path, minSearchTime=timeout, confidence=PIC_CONFIDENCE)
    except Exception as e:
        pmb.alert(error_message, title="警告", timeout=ALERT_TIMEOUT)
        print(error_message)
        return False
    
    try:
        inspect(locat)
        error_message = "位置错误:" + str(position) + ","
        ct = pg.center(locat)
        if position[0] == 'center':
            pass
        elif position[0] == 'left':
            ct = ct._replace(x=locat.left)
        elif position[0] == 'right':
            ct = ct._replace(x=locat.left + locat.width)
        elif position[0] == 'top':
            ct = ct._replace(y=locat.top)
        elif position[0] == 'bottom':
            ct = ct._replace(y=locat.top + locat.height)
        else:
            raise ValueError("There not " + position[0])
        
        cp = (ct.x+position[1][0], ct.y+position[1][1])
        inspect(cp)
    except Exception as e:
        error_message += str(e)
        pmb.alert(error_message, title="警告", timeout=ALERT_TIMEOUT)
        print(error_message)
        return False
    
    movetimes = MOVETIMES
    while movetimes >= 0:
        pg.moveTo(cp, duration=duration)
        movetimes -= 1
    
    return True