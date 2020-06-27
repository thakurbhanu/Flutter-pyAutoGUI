import pyautogui
import runFunctions

print('Creating Android Development Environment...')

pyautogui.sleep(4)


# ........................................................................................

# list_of_apps = ['youtube music', 'whatsapp', 'github', 'gitkraken', 'firefox','files', 'android studio', 'terminal',
#                 'brave',]

list_of_apps = ['youtube music', 'github', 'firefox','files', 'android studio', 'terminal',
                'brave',]
# ........................................................................................


def name_timer(nm):


    if nm == 'files':
        runFunctions.forFiles()

    elif nm == 'youtube music':
        runFunctions.twoSecondDelay(nm)
        runFunctions.threeSecondDelay('Whatsapp')
        pyautogui

    elif nm == 'android studio':
        runFunctions.sixSecondDelay(nm)

    elif nm == 'github':
        runFunctions.twoSecondDelay('gitkraken')
        runFunctions.threeSecondDelay(nm)

    elif nm == 'terminal':
        runFunctions.forEmulator('flutter emulator --launch pixel')
        runFunctions.forGpuStatistics('watch -n 2 nvidia-smi')
        runFunctions.forSystemMonitor()

for name in list_of_apps:

    pyautogui.hotkey('winleft', 'pagedown')
    name_timer(name)

# ........................................................................................