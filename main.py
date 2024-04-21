from cryptography.fernet import Fernet

# Function to generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# Generate a key
key = generate_key()

# The message to be encrypted
message = input("Write your message to encrypt: ")

# Encrypt the message
encrypted_message = encrypt_message(message, key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")