#%%
from cryptography.fernet import Fernet

#%% 透過密鑰加密資料
# 生成一個金鑰
key = Fernet.generate_key()
print(f"Key: {key}")

# 使用金鑰創建一個 Fernet 物件
cipher_suite = Fernet(key)

# 要加密的資料
data = "這是一段需要加密的資訊"
data = data.encode('utf-8')  # 將字串轉換為位元組

# 加密資料
encrypted_data = cipher_suite.encrypt(data)
print(f"Encrypted data: {encrypted_data}")


# 解密資料
decrypted_data = cipher_suite.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode('utf-8')  # 將位元組轉換回字串

print(f"Decrypted data: {decrypted_data}")


#%%
import os
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric.padding import MGF1
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# 使用者提供的密碼
password = "這是一個密碼"
password = password.encode('utf-8')  # 將字串轉換為位元組

# 生成一個隨機鹽
salt = os.urandom(16)

# 使用 PBKDF2 生成金鑰
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = urlsafe_b64encode(kdf.derive(password))  # 轉換為 Fernet 需要的格式

# 使用金鑰創建一個 Fernet 物件
cipher_suite = Fernet(key)

# 要加密的資料
data = "這是一段需要加密的資訊"
data = data.encode('utf-8')  # 將字串轉換為位元組

# 加密資料
encrypted_data = cipher_suite.encrypt(data)
print(f"Encrypted data: {encrypted_data}")

# 解密資料
decrypted_data = cipher_suite.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode('utf-8')  # 將位元組轉換回字串

print(f"Decrypted data: {decrypted_data}")
