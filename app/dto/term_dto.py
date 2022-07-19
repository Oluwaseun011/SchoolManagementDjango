class CreateTermDto:
    id: int
    session_id: int
    term_name: str
    term_status: str


class EditTermDto:
    id: int
    term_name: str


class ListTermDto:
    session_name: str
    term_name: str
    term_status: str



class GetTermDto:
    id: int
    session_id: int
    term_name: str
    term_status: str
