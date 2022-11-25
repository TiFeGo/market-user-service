from typing import Union
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


def verify_password(plain_password: Union[str, bytes], hashed_password: Union[str, bytes]) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: Union[str, bytes]):
    return pwd_context.hash(password)
