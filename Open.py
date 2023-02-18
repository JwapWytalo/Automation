import pyautogui
import time


pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('Enter')

time.sleep(2)

pyautogui.press('Tab')
pyautogui.press('Enter')


time.sleep(1)

pyautogui.write('https://github.com/JwapWytalo')
pyautogui.press('Enter')

time.sleep(2)

pyautogui.hotkey('Ctrl', ('t'))
pyautogui.write('https://si3.ufc.br/sigaa/verTelaLogin.do')
time.sleep(1)
pyautogui.press('Enter')

time.sleep(2)

pyautogui.press('Enter')

time.sleep(2)


pyautogui.hotkey('Ctrl', ('t'))
pyautogui.write('https://www.youtube.com/')
time.sleep(1)
pyautogui.press('Enter')

time.sleep(2)

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('Enter')

time.sleep(1)

pyautogui.press(['Tab']*4)
pyautogui.press('Enter')

time.sleep(2)

pyautogui.write('https://chat.openai.com/chat')
pyautogui.press('Enter')

time.sleep(2)

pyautogui.moveTo(1905, 1067, duration=1)
pyautogui.click(1905, 1067)






