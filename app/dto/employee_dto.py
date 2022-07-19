import datetime


class CreateEmployeeDto:
    id: int
    staff_number: str
    person_id: int
    employment_date: datetime
    employment_status: str


class EditEmployeeDto:
    id: int
    staff_number: str


class ListEmployeeDto:
    employee_name: str
    gender: str
    employment_status: str


class GetEmployeeDto:
    id: int
    staff_number: str
    person_id: int
    employment_date: datetime
    employment_status: str
