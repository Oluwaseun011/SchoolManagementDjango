class RegisterStudentDto:
    id: int
    admin_number: str
    admin_year: str
    person_id: int


class EditStudentDto:
    id: int
    admin_number: str


class ListStudentDto:
    id: int
    student_name: str
    admin_number: str
    basic: str


class GetStudentDto:
    id: int
    admin_number: str
    person_id: int
