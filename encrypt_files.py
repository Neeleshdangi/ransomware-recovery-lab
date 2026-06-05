from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print("Simulation Script")
print("Demonstrates file encryption process")
