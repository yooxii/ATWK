import win32api
import win32gui
from win32con import WM_INPUTLANGCHANGEREQUEST
import ctypes

# 定义常量
VK_CAPITAL = 0x14  # Caps Lock 键的虚拟键码
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002

def is_caps_lock_on():
    """检测 Caps Lock 键是否开启"""
    return bool(ctypes.WinDLL('user32', use_last_error=True).GetKeyState(VK_CAPITAL))

def toggle_caps_lock():
    """切换 Caps Lock 键的状态"""
    if is_caps_lock_on():
        # 如果 Caps Lock 开启，模拟按下并释放 Caps Lock 键
        ctypes.WinDLL('user32', use_last_error=True).keybd_event(VK_CAPITAL, 0, KEYEVENTF_EXTENDEDKEY, 0)
        ctypes.WinDLL('user32', use_last_error=True).keybd_event(VK_CAPITAL, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)

def change_language(language="EN"):
    """
    切换语言
    :param language: EN––English; ZH––Chinese
    :return: bool
    """
    LANGUAGE = {
        "CH": 0x0804,
        "EN": 0x0409
    }
    """
    获取键盘布局
    """
    # im_list = win32api.GetKeyboardLayoutList()
    # im_list = list(map(hex, im_list))
    # print(im_list)
    
    hwnd = win32gui.GetForegroundWindow()
    language = LANGUAGE.get(language)
    result = win32api.SendMessage(
        hwnd,
        WM_INPUTLANGCHANGEREQUEST,
        0,
        language
    )
    toggle_caps_lock()
    return result == 0

if __name__ == '__main__':
    change_language("EN")