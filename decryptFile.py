
# 1) read the key from file
key = ''
with open('myTopSecretkey.key', 'rb') as file:
    key = file.read()


# 2)read the encrypted data from file
encryptedData = ''
with open('myTopSecretInfo.txt', 'rb') as file:
    encryptedData = file.read()



# 3) decrypt the data
from cryptography.fernet import Fernet

f = Fernet(key)

decryptedData = f.decrypt(encryptedData)



print('Encrypted data:',encryptedData.decode())

print()

print('Decrypted data:',decryptedData.decode())