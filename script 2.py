import hashlib
import subprocess
import os
import pefile

def calculate_hashes(file_path):
    # Calculate MD5, SHA-1, and SHA-256 hashes
    hashes = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}

    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            for h in hashes.values():
                h.update(chunk)

    for name, hash_obj in hashes.items():
        print(f"{name.upper()} Hash: {hash_obj.hexdigest()}")

def extract_strings(file_path):
    # Extract strings using the specified path to 'strings64.exe'
    print("\nExtracted Strings:")
    strings_path = 'C:\\Users\\MRUDULA\\strings64.exe'  # Path to the strings executable
    try:
        result = subprocess.run([strings_path, file_path], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print(f"Error: 'strings' utility not found at {strings_path}. Ensure the path is correct.")

# Example usage
file_path = 'C:\\Users\\MRUDULA\\OneDrive\\Desktop\\npp.8.6.7.Installer.exe'  # Replace with the correct .exe file name
calculate_hashes(file_path)
extract_strings(file_path)
