
# 1) read key from file
key = ''
with open('myTopSecretkey.key', 'rb') as file:
    key = file.read()
# 2) read data from file
data = ''
with open('toBeSecret.txt', 'rb') as file:
    data = file.read()

#  3) encrypt data
from cryptography.fernet import Fernet

f = Fernet(key)

encryptedData = f.encrypt(data)


# 4) save the encrypted data into file
with  open ('myTopSecretInfo.txt','wb') as file:
    file.write(encryptedData)