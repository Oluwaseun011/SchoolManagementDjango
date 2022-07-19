from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.dto.permission_dto import *
from app.models import Permission, Person, Role


class PermissionRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_permission(self, model: CreatePermissionDto):
        """Create Permission Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_permission(self, permission_id: int, model: EditPermissionDto):
        """Edit Permission Object"""
        raise NotImplementedError

    @abstractmethod
    def list_permission(self) -> List[ListPermissionDto]:
        """List Permission Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_permission(self, permission_id: int) -> GetPermissionDto:
        """Get Permission Object"""
        raise NotImplementedError

    @abstractmethod
    def assign_permission_to_role(self, model: AssignPermissionToRoleDto):
        """Assign Permission to Role"""
        raise NotImplementedError

    @abstractmethod
    def assign_permission_to_person(self, model: AssignPermissionToUserDto):
        """Assign Permission to Person"""
        raise NotImplementedError


class DjangoORMPermissionRepository(PermissionRepository):
    def create_permission(self, model: CreatePermissionDto):
        permission = Permission()
        permission.id = model.id
        permission.name = model.name
        permission.description = model.description
        permission.save()

    def edit_permission(self, permission_id: int, model: EditPermissionDto):
        try:
            permission = Permission.objects.get(id=permission_id)
            permission.name = model.name
            permission.description = model.description
            permission.save()
        except Permission.DoesNotExist as e:
            return e

    def list_permission(self) -> List[ListPermissionDto]:
        permissions = Permission.objects.all()
        result: List[ListPermissionDto] = []

        for permission in permissions:
            item = ListPermissionDto()
            item.name = permission.name
            result.append(item)
        return result

    def get_permission(self, permission_id: int) -> GetPermissionDto:
        permission = Permission.objects.get(id=permission_id)
        item = GetPermissionDto()
        item.id = permission.id
        item.name = permission.name
        item.description = permission.description
        return item

    def assign_permission_to_person(self, model: AssignPermissionToUserDto):
        try:
            permission = Permission.objects.get(id=model.permission_id)
            Person.objects.get(id=model.person_id).permission.add(permission)
        except Exception as e:
            return e

    def assign_permission_to_role(self, model: AssignPermissionToRoleDto):
        try:
            permission = Permission.objects.get(id=model.permission_id)
            Role.objects.get(id=model.role_id).permission.add(permission)
        except Exception as e:
            return e
