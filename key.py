from cryptography.fernet import Fernet
import os

def generate_and_save_key(filename):
    key = Fernet.generate_key()
    with open(filename, 'wb') as f:
        f.write(key)
    print("Key saved to", filename)

if __name__ == "__main__":
    # Prompt for the filename or full path to save the key
    filename = input("Enter filename or full path to save the key (e.g., /path/to/encryption_key.key): ")

    # Validate directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
    else:
        # Generate a key and save it to the specified file
        generate_and_save_key(filename)


