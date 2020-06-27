import pyautogui
import delaySeconds, winPressFun


def forFiles():

    pyautogui.sleep(2)
    pyautogui.hotkey('winleft', 'e')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrlleft', 'f')
    pyautogui.sleep(2)
    pyautogui.typewrite('FlutterLearn')
    delaySeconds.twoSecs()
    pyautogui.sleep(1)

def forEmulator(commandString):

    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.sleep(2)
    pyautogui.typewrite(commandString)
    delaySeconds.twoSecs()


def forGpuStatistics(commandString):

    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.sleep(2)
    pyautogui.typewrite(commandString)
    delaySeconds.threeSecs()

def forSystemMonitor():
    winPressFun.winButtonPress()
    pyautogui.typewrite('System Monitor')
    delaySeconds.threeSecs()

def twoSecondDelay(termTwo):
    winPressFun.winButtonPress()
    pyautogui.typewrite(termTwo)
    delaySeconds.twoSecs()

def threeSecondDelay(threeSeconds):
    winPressFun.winButtonPress()
    pyautogui.typewrite(threeSeconds)
    delaySeconds.threeSecs()

def sixSecondDelay(threeSeconds):
    winPressFun.winButtonPress()
    pyautogui.typewrite(threeSeconds)
    delaySeconds.sixSecs()
