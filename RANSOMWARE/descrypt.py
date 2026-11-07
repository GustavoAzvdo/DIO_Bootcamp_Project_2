from cryptography.fernet import Fernet
import os

#1. Push a key for decryption

def load_key():
    return open("secret.key", "rb").read()

#2. Decrypt a file
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

#3. Search for files to decrypt
def search_files(directory, extension):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

#4. Main function to execute the decryption
def main():
    key = load_key()
    files = search_files("test_files", ".txt")
    for file in files:
        decrypt_file(file, key)
    print("Decryption complete. Thx ;)")

if __name__ == "__main__":
    main()