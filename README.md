# 🔐 Password Manager - Generador y Gestor Básico

Un proyecto sencillo pero útil para **gestionar contraseñas de forma segura**.  
Genera claves aleatorias, las cifra localmente y permite consultarlas cuando sea necesario.

---

## 🚀 Características
- Generador de contraseñas seguras con longitud personalizable.
- Opción de incluir símbolos, números y letras.
- Almacenamiento cifrado con **AES (Fernet)**.
- Listado de servicios guardados con descifrado automático.
- Base de datos local (`passwords.json`) protegida con clave (`secret.key`).

---

## 📦 Instalación
Clona este repositorio y entra en la carpeta:

```bash
git clone https://github.com/tuusuario/password-manager.git
cd password-manager
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso
Ejecuta el script:

```bash
python password_manager.py
```

### Menú principal
- Generar contraseña segura.
- Guardar nueva contraseña.
- Ver contraseñas guardadas.
- Salir.

---

## 📂 Archivos
- `password_manager.py` → código principal.
- `passwords.json` → base local de contraseñas cifradas.
- `secret.key` → clave usada para el cifrado/descifrado.
- `requirements.txt` → dependencias.

---

## ⚠️ Nota de Seguridad
Este proyecto es educativo. No está pensado para reemplazar gestores profesionales como Bitwarden o KeePass.  
La base de datos se guarda en local, y la seguridad depende de proteger tu `secret.key`.