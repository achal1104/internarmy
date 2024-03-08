# 0) pip install cryptography

# 1) Generate a symmetric key
from  cryptography.fernet import Fernet
key = Fernet.generate_key() 


# 2) save the key into a file
with open('myTopSecretkey.key', 'wb') as file:
    file.write(key)