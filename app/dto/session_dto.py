import datetime


class CreateSessionDto:
    id: int
    session_name: str
    session_start: datetime
    session_end: datetime
    session_status: str


class EditSessionDto:
    id: int
    session_name: str
    session_start: datetime
    session_end: datetime


class ListSessionDto:
    session_name: str
    session_status: str


class GetSessionDto:
    id: int
    session_name: str
    session_start: datetime
    session_end: datetime
    session_status: str