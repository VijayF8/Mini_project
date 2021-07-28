from cryptography.fernet import Fernet
file = open('file name where the key is stored.key', 'rb')
key = file.read() # The key will be type bytes
file.close() # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = 'the file name which is encrypted.encrypted'
output_file = 'the file which stores the data.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)