from cryptography.fernet import Fernet
from django.conf import settings


def encrypt_text(text):
    if not text:
        return text
    text = text.encode()
    crypto = Fernet(settings.ENCRYPTION_KEY)
    return crypto.encrypt(text).decode()


def decrypt_text(text):
    if not text:
        return text
    text = text.encode()
    crypto = Fernet(settings.ENCRYPTION_KEY)
    return crypto.decrypt(text).decode()
