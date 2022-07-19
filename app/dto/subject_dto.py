class CreateSubjectDto:
    id: int
    subject_name: str


class EditSubjectDto:
    id: int
    subject_name: str


class ListSubjectDto:
    subject_name: str


class GetSubjectDto:
    id: int
    subject_name: str
