import datetime


class CreatePersonDto:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    address: str
    gender: str
    telephone: str
    date_of_birth: datetime
    date_created: datetime


class EditPersonDto:
    id: int
    first_name: str
    last_name: str
    email: str
    address: str
    gender: str
    telephone: str
    date_of_birth: datetime
    date_updated: datetime


class ListPersonDto:
    name: str
    gender: str


class GetPersonDto:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    gender: str
    telephone: str
    date_of_birth: datetime
    date_created: datetime


class AuthenticateDto:
    id: int
    email: str
    password: str


class ChangePasswordDto:
    id: int
    email: str
    new_password: str
