from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import secrets

def encrypt_column_aes256_ultra(value):
    """
    Encripta un valor usando AES-256 CBC. Devuelve base64 o None si hay error.
    """
    if value is None:
        return None

    key = b'12345678901234567890123456789012'  # 32 bytes para AES-256

    try:
        text_str = str(value)
        data_padded = pad(text_str.encode('utf-8'), AES.block_size)
        iv = secrets.token_bytes(16)  # IV único por registro
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(data_padded)
        return base64.b64encode(iv + encrypted_data).decode('utf-8')
    except Exception:
        return None
