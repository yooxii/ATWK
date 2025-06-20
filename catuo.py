import pyautogui as pg
import mypymsgbox as pmb

from rich import inspect

# 定义常用位置
PCENTER = ["center", (0, 0)]
PLEFT = ["left", (5, 0)]
PRIGHT = ["right", (-5, 0)]
PTOP = ["top", (0, 5)]
PBOTTOM = ["bottom", (0, -5)]

# 一些配置

# 警告框超时时间，1000ms
ALERT_TIMEOUT = 1000
MOVETIMES = 5
PIC_CONFIDENCE = 0.96


def exists_image(
    image_path,
    minSearchTime=1.0,
    region: tuple[int, int, int, int] = None,
    confidence=PIC_CONFIDENCE,
):
    """检测屏幕是否存在匹配的图像。

    Args:
        image_path (str): 图像路径
        minSearchTime (float, optional): 超时时间. 默认值: 1.0.
        region (tuple[int,int,int,int], optional): 限制区域寻找. 默认值: None.

    Returns:
        bool: 成功匹配返回True，否则返回False
    """
    try:
        pg.locateOnScreen(
            image_path,
            minSearchTime=minSearchTime,
            region=region,
            confidence=confidence,
        )
        return True
    except:
        return False


def moveTo_image(
    image_path, position=PCENTER, duration=0.0, wait_time=0.3, timeout=5.0
):
    """移动鼠标到屏幕图像匹配位置。

    Args:
        image_path (str): 图片路径
        position (list, optional): 图像内部位置. 默认值: PCENTER.
        duration (float, optional): 鼠标移动速度. 默认值: 0.0.
        wait_time (float, optional): 鼠标移动前等待时间. 默认值: 0.3.
        timeout (float, optional): 图像匹配超时时间. 默认值: 5.0.

    Raises:
        ValueError: 图像内部位置错误

    Returns:
        bool: 成功匹配返回True，否则返回False
    """
    pg.sleep(wait_time)
    error_message = ""

    try:
        error_message = "未找到 " + image_path.split("\\")[-1]
        locat = pg.locateOnScreen(
            image_path, minSearchTime=timeout, confidence=PIC_CONFIDENCE
        )
    except Exception as e:
        pmb.alert(error_message, title="警告", timeout=ALERT_TIMEOUT)
        print(error_message)
        return False

    try:
        # inspect(locat)
        error_message = "位置错误:" + str(position) + ","
        ct = pg.center(locat)
        if position[0] == "center":
            pass
        elif position[0] == "left":
            ct = ct._replace(x=locat.left)
        elif position[0] == "right":
            ct = ct._replace(x=locat.left + locat.width)
        elif position[0] == "top":
            ct = ct._replace(y=locat.top)
        elif position[0] == "bottom":
            ct = ct._replace(y=locat.top + locat.height)
        else:
            raise ValueError("There not " + position[0])

        cp = (ct.x + position[1][0], ct.y + position[1][1])
        # inspect(cp)
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


def click_image(
    image_path, position=PCENTER, duration=0.0, wait_time=0.3, timeout=5.0, clicks=1
):
    if moveTo_image(image_path, position, duration, wait_time, timeout):
        pg.click(clicks=clicks)


if __name__ == "__main__":
    print(
        pg.locateOnScreen(
            ".\\Pic_lib\\six_1.png",
            region=(300, 500, 700, 1000),
            minSearchTime=1.5,
            confidence=0.96,
        )
    )
