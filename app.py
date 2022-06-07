import pygame
import sys
import os
import time

from pynput import keyboard


if getattr(sys, 'frozen', False): workspace = os.path.dirname(sys.executable) # In .exe
elif __file__: workspace = os.path.dirname(os.path.abspath(__file__)) # In .py script

sounds = os.path.join(workspace, 'sounds')

pygame.mixer.init()
sound_keyup = pygame.mixer.Sound(os.path.join(sounds,'keyup.mp3'))
sound_keydown = pygame.mixer.Sound(os.path.join(sounds,'keydown.mp3'))
sound_returnup = pygame.mixer.Sound(os.path.join(sounds,'carriage-return-start.mp3'))
sound_returndown = pygame.mixer.Sound(os.path.join(sounds,'carriage-return-end.mp3'))
sound_spacebar = pygame.mixer.Sound(os.path.join(sounds,'spacebar.mp3'))
sound_bell = pygame.mixer.Sound(os.path.join(sounds,'bell.mp3'))


pressed_list = []

def handle_release(key):
    Key = str(key)

    if Key in pressed_list:
        pressed_list.remove(Key)

    print(f"{Key} released")

    # Key event
    if Key == "Key.enter":
        sound_bell.play()
        # Wait for sound to stop
        while pygame.mixer.get_busy():
            time.sleep(0.1)
        sound_returnup.play()
    else:
        sound_keyup.play()

def handle_press(key):
    Key = str(key)

    if Key in pressed_list:
        return
    else:
        pressed_list.append(Key)
    
    print(f"{Key} pressed")

    # Key event
    if Key == "Key.space":
        sound_spacebar.play()
    elif Key == "Key.backspace":
        sound_spacebar.play()
    elif Key == "Key.enter":
        sound_returndown.play()
    else:
        sound_keydown.play()


# Listen for keypress
with keyboard.Listener(on_release = handle_release, on_press=handle_press) as listener:
    listener.join()