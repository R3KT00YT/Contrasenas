"""
Password Manager - Generador y Gestor Básico de Contraseñas
------------------------------------------------------------
- Genera contraseñas seguras aleatorias.
- Permite guardar contraseñas cifradas en un archivo local.
- Muestra el listado de cuentas guardadas.
- Descifra las contraseñas cuando se necesitan.

Uso:
    python password_manager.py
"""

import os
import json
import base64
import secrets
import string
from cryptography.fernet import Fernet

# ------------------------
# CONFIGURACIÓN
# ------------------------
DB_FILE = "passwords.json"
KEY_FILE = "secret.key"


# ------------------------
# FUNCIONES DE SEGURIDAD
# ------------------------
def load_key():
    """Carga la clave de cifrado o la crea si no existe."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)


def generate_password(length=16, use_symbols=True):
    """Genera una contraseña segura aleatoria."""
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    return ''.join(secrets.choice(alphabet) for _ in range(length))


def save_password(service, username, password, fernet):
    """Guarda un registro cifrado en la base local."""
    data = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    encrypted = fernet.encrypt(password.encode()).decode()
    data[service] = {"username": username, "password": encrypted}

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[✔] Contraseña guardada para {service}")


def list_passwords(fernet):
    """Lista todos los servicios guardados con sus contraseñas descifradas."""
    if not os.path.exists(DB_FILE):
        print("[!] No hay contraseñas guardadas aún.")
        return

    with open(DB_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n=== Gestor de Contraseñas ===")
    for service, creds in data.items():
        decrypted = fernet.decrypt(creds["password"].encode()).decode()
        print(f"- Servicio: {service}")
        print(f"  Usuario : {creds['username']}")
        print(f"  Password: {decrypted}")
        print("-----------------------------")


# ------------------------
# MENÚ PRINCIPAL
# ------------------------
def main():
    fernet = load_key()

    while True:
        print("\n=== Password Manager ===")
        print("1. Generar contraseña segura")
        print("2. Guardar nueva contraseña")
        print("3. Ver contraseñas guardadas")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            length = int(input("Longitud (ej. 16): ") or 16)
            symbols = input("¿Usar símbolos? (s/n): ").lower() == "s"
            pwd = generate_password(length, symbols)
            print(f"[+] Contraseña generada: {pwd}")

        elif choice == "2":
            service = input("Servicio (ej. Gmail): ")
            username = input("Usuario: ")
            pwd_choice = input("¿Quieres generar contraseña automáticamente? (s/n): ").lower()
            if pwd_choice == "s":
                pwd = generate_password()
            else:
                pwd = input("Introduce tu contraseña: ")
            save_password(service, username, pwd, fernet)

        elif choice == "3":
            list_passwords(fernet)

        elif choice == "4":
            print("Saliendo... 👋")
            break

        else:
            print("[!] Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
