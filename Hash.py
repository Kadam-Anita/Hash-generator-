import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken


# ----- Encryption -----
def encrypt_message(password: str, message: str) -> tuple:
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return base64.urlsafe_b64encode(salt).decode(), encrypted.decode()


# ----- Decryption -----
def decrypt_message(password: str, salt_b64: str, encrypted_b64: str) -> str:
    try:
        salt = base64.urlsafe_b64decode(salt_b64)
        encrypted = encrypted_b64.encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted)
        return decrypted.decode()
    except InvalidToken:
        return "❌ Decryption failed: Wrong password or data."
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ----- Main Interactive Loop -----
if __name__ == "__main__":
    last_encrypted = ""
    last_salt = ""

    while True:
        print("\n✨Welcome to Cryptographic hash world...#️⃣ 🧑‍💻✨")
        print("1. Encrypt a message")
        print("2. Decrypt the last encrypted message")
        print("3. Decrypt a custom message")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            password = input("🔐 Enter password: ")
            message = input("📝 Enter message to encrypt: ")

            last_salt, last_encrypted = encrypt_message(password, message)

            print("\n✅ Encrypted successfully!")
            print("\n🔒 Encrypted Message (Base64):", last_encrypted)
            print("\n🔑 Salt (Base64):", last_salt)

        elif choice == "2":
            if not last_encrypted or not last_salt:
                print("⚠️ No message encrypted yet!")
                continue

            password = input("🔐 Enter password to decrypt: ")
            result = decrypt_message(password, last_salt, last_encrypted)
            print("🗝️ Decrypted Message:", result)

        elif choice == "3":
            password = input("🔐 Enter password: ")
            encrypted = input("📄 Enter encrypted message (Base64): ")
            salt = input("🧂 Enter salt (Base64): ")
            result = decrypt_message(password, salt, encrypted)
            print("🗝️ Decrypted Message:", result)

        elif choice == "4":
            print("👋 Exiting... Thank you for coming♥️ , Goodbye!")
            break

        else:
            print("❗ Invalid choice, try again.")
