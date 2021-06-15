from selenium import webdriver
from pynput import keyboard

driver = webdriver.Chrome('C:/Users/ferdz/Desktop/Tools/chromedriver.exe')

driver.get('http://localhost/')

# The key combination to check
keyComb = [keyboard.Key.ctrl_l, '\x13']

# The currently active modifiers
current = []

def refreshPage():
  print(f'Refreshing Page: {driver.current_url}')
  driver.refresh()
  print('Page refreshed')

def on_press(key):
    current.append(key)
    # print("Current Key: ", key, type(key))
    # print(f'Key Comb: {keyComb}')
    # print('Keys Pressed: ', current)
    if all(k in keyComb for k in current):
        refreshPage()
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    try:
      if len(current) >= 2:
        current.clear()
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()