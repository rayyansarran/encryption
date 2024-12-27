import os
from cryptography.fernet import Fernet
import base64
import time

def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    return decrypted_text

def encrypt_file(filename, key, output_directory):
    with open(filename, 'rb') as f:
        data = f.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    encrypted_filename = os.path.join(output_directory, os.path.basename(filename) + '.encrypted')
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(filename, key, output_directory):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_filename = os.path.join(output_directory, os.path.basename(filename)[:-len('.encrypted')])
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

def encrypt_image(filename, key, output_directory):
    with open(filename, 'rb') as f:
        data = f.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    encrypted_filename = os.path.join(output_directory, os.path.basename(filename) + '.encrypted')
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_image(filename, key, output_directory):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_filename = os.path.join(output_directory, os.path.basename(filename)[:-len('.encrypted')])
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

def save_encrypted_text_to_file(encrypted_text, file_path):
    with open(file_path, 'wb') as f:
        f.write(encrypted_text)

if __name__ == "__main__":
    while True:
        time.sleep(1)
        
        # Ask whether to perform encryption or decryption
        action = input("Do you want to:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice (1/2/3): ")

        if action == '1':

            # Ask the user for the type of data to encrypt
            data_type = input("1. Text\n2. File\n3. Image\nEnter choice (1/2/3): ")

            if data_type == '1':
                # Encrypt text
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                text = input("Enter text to encrypt: ")
                encrypted_text = encrypt_text(text, key)
                encrypted_text_base64 = base64.b64encode(encrypted_text).decode()
                print("Encrypted text (base64):", encrypted_text_base64)

                # Save encrypted text to a file
                save_encrypted_text_to_file(encrypted_text, 'encrypted_text.txt')

            elif data_type == '2':
                # Ask for the directory to store encrypted files
                output_directory = input("Enter directory to store encrypted files: ")

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Encrypt file
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                file_name = input("Enter file name to encrypt: ")
                encrypt_file(file_name, key, output_directory)

                time.sleep(1)
                
                print("Encrypted successfully.")

            elif data_type == '3':
                # Ask for the directory to store encrypted files
                output_directory = input("Enter directory to store encrypted images: ")

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                    
                # Encrypt image
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                image_name = input("Enter image name to encrypt: ")
                encrypt_image(image_name, key, output_directory)

                time.sleep(1)
                
                print("Encrypted successfully.")
            
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")


        elif action == '2':
            # Ask the user for the type of data to decrypt
            data_type = input("1. Text\n2. File\n3. Image\nEnter choice (1/2/3): ")


            if data_type == '1':
                # Decrypt text
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                encrypted_text_base64 = input("Enter base64-encoded encrypted text: ")
                encrypted_text = base64.b64decode(encrypted_text_base64)
                decrypted_text = decrypt_text(encrypted_text, key)
                print("Decrypted text:", decrypted_text)

            elif data_type == '2':
                # Ask for the directory to store decrypted files
                output_directory = input("Enter directory to store decrypted files: ")

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Decrypt file
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                file_name = input("Enter file name to decrypt: ")
                decrypt_file(file_name, key, output_directory)
                
                time.sleep(1)
                
                print("Decrypted successfully.")

            elif data_type == '3':
                # Ask for the directory to store decrypted files
                output_directory = input("Enter directory to store decrypted images: ")

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Decrypt image
                key_file = input("Enter path to the key file: ")
                with open(key_file, 'rb') as f:
                    key = f.read()
                image_name = input("Enter image name to decrypt: ")
                decrypt_image(image_name, key, output_directory)

                time.sleep(1)
                
                print("Decrypted successfully.")

            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

        elif action == '3':
            print("Exiting...")
            time.sleep(1)
            print("Exited")
            time.sleep(1)
            break



        else:
            print("Invalid choice. Please enter a number from 1 to 3.")
