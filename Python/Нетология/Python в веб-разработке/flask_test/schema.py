import pydantic
from abc import ABC
from typing import Optional

# с помощью ABC - указываем что этот класс абстрактный
class AbstractUser(pydantic.BaseModel, ABC):
    name: str
    password: str

    # перенесли этот метод из кода ниже сюда - чтоб не повторяться
    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length = 8")
        return v


# создание пользователя
class CreateUser(AbstractUser):
    # нам должны прийти имя - строка и пароль - строка
    name: str
    password: str

    # # добавим проверку на минимальную длину пароля
    # # первый декоратор - нужен чтоб мы проверяли только поле password
    # # второй чтоб не надо было принимать self
    # @pydantic.field_validator("password")
    # @classmethod
    # def secure_password(cls, v: str) -> str:
    #     if len(v) < 8:
    #         raise ValueError(f"Minimal length = 8")
    #     return v


# обновление пользователя
class UpdateUser(AbstractUser):
    # нам могут прийти одно из этих полей или вообще не прийти
    # поэтому ставим Optional и ставим значение по умолчанию None
    name: Optional[str] = None
    password: Optional[str] = None

    # # добавим проверку на минимальную длину пароля
    # # первый декоратор - нужен чтоб мы проверяли только поле password
    # # второй чтоб не надо было принимать self
    # @pydantic.field_validator("password")
    # @classmethod
    # def secure_password(cls, v: str) -> str:
    #     if len(v) < 8:
    #         raise ValueError(f"Minimal length = 8")
    #     return v
