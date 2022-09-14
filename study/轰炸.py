"""轰炸"""
import time
from pynput import mouse
from pynput import keyboard


def keyboard_input(string):
    """键盘输入
    :param string:
    """
    key1 = keyboard.Controller()
    key1.type(string)
    key1.press(keyboard.KeyCode.from_vk(13))


def mouse_click():
    """控制鼠标点击发送
"""
    mouse1 = mouse.Controller()
    mouse1.press(mouse.Button.left)
    mouse1.release(mouse.Button.left)


def hz(number, string):
    """
    :param number:次数
    :param string:轰炸内容
    """
    time.sleep(5)
    for i in range(number):
        keyboard_input(string+str(i))  # 键盘输入
        mouse_click()
        time.sleep(0.1)


if __name__ == '__main__':
    hz(50, "你快出来啊")
