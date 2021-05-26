
from pynput import keyboard
from pynput.keyboard import KeyCode, Controller
from playsound import playsound
from typing import List
import time
pressed = set()
cont = Controller()

def main() -> None:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    while True:
        time.sleep(0.0025)
        continue #not elegant but works for now


def on_press(key):

    try:
        global pressed
        k = str(key).lower()

        if(key in pressed): #prevents constant restaring of the note when key is held
            return
        elif key == keyboard.Key.shift:
            playsound("cNote.wav", False)
        elif key == KeyCode.from_char('a') or key == KeyCode.from_char('A'):
            playsound("piano-c_C#_major.wav", False)
        elif key == KeyCode.from_char('z') or key == KeyCode.from_char('Z'):#d
            playsound("piano-d_D_major.wav", False)
        elif key == KeyCode.from_char('s')or key == KeyCode.from_char('S'):
            playsound("piano-eb_D#_major.wav", False)
        elif key == KeyCode.from_char('x')or key == KeyCode.from_char('X'):
            playsound("piano-e_E_major.wav", False)
        elif key ==KeyCode.from_char('c')or key == KeyCode.from_char('C'):
            playsound("piano-f_F_major.wav", False)
        elif key ==KeyCode.from_char('f')or key == KeyCode.from_char('F'):
            playsound("piano-f_F#_major.wav", False)
        elif key ==KeyCode.from_char('v')or key == KeyCode.from_char('V'):
            playsound("piano-g_G_major.wav", False)
        elif key ==KeyCode.from_char('g')or key == KeyCode.from_char('G'):
            playsound("piano-g_G#_major.wav", False)
        elif key ==KeyCode.from_char('b')or key == KeyCode.from_char('B'):
            playsound("piano-a_A_major.wav", False)
        elif key ==KeyCode.from_char('h') or key == KeyCode.from_char('H'):
            playsound("piano-bb_A#_major.wav", False)
        elif key ==KeyCode.from_char('n')or key == KeyCode.from_char('N'):
            playsound("piano-b_B_major.wav", False)

        pressed.add(key)
        return
         #couldnt find a free download for last key

    except AttributeError:
        print("error")

def on_release(key):
    global pressed
    if key in pressed:
        pressed.remove(key)

if __name__ == "__main__":
    main()
