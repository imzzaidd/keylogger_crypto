from cryptography.fernet import Fernet
import os

LOG_FILE = "logs/log.txt"
ENCRYPTED_FILE = "logs/log_encrypted.txt"
KEY_FILE = "logs/secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_log():
    key = load_key()
    fernet = Fernet(key)

    with open(LOG_FILE, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)
    with open(ENCRYPTED_FILE, "wb") as enc_file:
        enc_file.write(encrypted)
    print(f"Archivo cifrado guardado como {ENCRYPTED_FILE}")

if __name__ == "__main__":
    encrypt_log()