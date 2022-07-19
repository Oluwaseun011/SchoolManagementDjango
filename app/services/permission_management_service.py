from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.dto.permission_dto import *
from app.models import Permission, Person, Role
from app.repositories.permission_repository import PermissionRepository, DjangoORMPermissionRepository


class PermissionManagementService(metaclass=ABCMeta):
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


class DefaultPermissionManagementService(PermissionManagementService):
    repository: PermissionRepository

    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def create_permission(self, model: CreatePermissionDto):
        permission = Permission.objects.get(name=model.name)
        if isinstance(permission, (GetPermissionDto,)):
            return False
        else:
            return self.repository.create_permission(model)

    def edit_permission(self, permission_id: int, model: EditPermissionDto):
        result = self.repository.edit_permission(permission_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_permission(self) -> List[ListPermissionDto]:
        return self.repository.list_permission()

    def get_permission(self, permission_id: int) -> GetPermissionDto:
        result = self.repository.get_permission(permission_id)
        if isinstance(result, (GetPermissionDto,)):
            return result
        else:
            return False

    def assign_permission_to_role(self, model: AssignPermissionToRoleDto):
        result = self.repository.assign_permission_to_role(model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def assign_permission_to_person(self, model: AssignPermissionToUserDto):
        result = self.repository.assign_permission_to_person(model)
        if isinstance(result, (Exception,)):
            return False
        return True
