import datetime


class CreateApplicationDto:
    id: int
    basic_id: int
    application_no: str
    email: str
    first_name: str
    last_name: str
    status: str
    application_score: int
    passport: str
    date_created: datetime


class EditApplicationDto:
    id: int
    email: str
    first_name: str
    last_name: str
    status: str
    passport: str
    date_updated: datetime


class ListApplicationDto:
    applicants: str
    status: str


class GetApplicationDto:
    id: int
    email: str
    first_name: str
    last_name: str
    status: str
    passport: str


class ActivateApplicationDto:
    id: int
    status: str
