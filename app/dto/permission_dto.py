class CreatePermissionDto:
    id: int
    name: str
    description: str


class EditPermissionDto:
    id: int
    name: str
    description: str


class ListPermissionDto:
    name: str


class GetPermissionDto:
    id: int
    name: str
    description: str


class AssignPermissionToRoleDto:
    permission_id: int
    role_id: int


class AssignPermissionToUserDto:
    permission_id: int
    person_id: int
