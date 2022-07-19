class CreateRoleDto:
    id: int
    name: str
    description: str


class ListRoleDto:
    name: str


class EditRoleDto:
    id: int
    name: str
    description: str


class GetRoleDto:
    id: int
    name: str
    description: str


class AssignRoleToUserDto:
    person_id: int
    role_id: int
