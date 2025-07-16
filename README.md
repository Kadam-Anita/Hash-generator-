# Hash-generator-
You can code your message in terms of hash value to send the message safely to other person. This Python script allows you to encrypt and decrypt messages using a password. It uses secure cryptographic techniques to ensure your message stays private and safe.

🚀 What Can This Script Do?

✅ Encrypt any message using a password

✅ Decrypt a previously encrypted message

✅ Decrypt a custom message and salt that you’ve saved earlier

✅ Reuse the last message without restarting the program

🛠️ How It Works

Your message is encrypted using AES-256 (via Fernet)

A secure key is created from your password using PBKDF2 with SHA-256 and a random salt

The salt and encrypted message are shown in Base64 so you can save or share them safely

To decrypt, use the same password and salt

📦 Requirements

Make sure you have Python installed, then install the cryptography library:

>> pip install cryptography

🎯 Use Cases of This Project

This encryption project is useful in real-world scenarios where you need to protect sensitive messages using only a password — without needing complex key management.

✨ Real-World Uses

🔐 1. Secure Messaging Without Internet
🧳 2. Travel Documents or IDs Backup
🗂️ 3. Password-Protected Note/Diary App




