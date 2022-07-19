from abc import abstractmethod, ABCMeta
from app.models import Role, Person
from app.dto.role_dto import *
from typing import List, Union
from app.repositories.role_repository import RoleRepository, DjangoORMRoleRepository


class RoleManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_role(self, model: CreateRoleDto):
        """Create Role Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_role(self, role_id: int, model: EditRoleDto):
        """Edit Role Object"""
        raise NotImplementedError

    @abstractmethod
    def list_role(self) -> List[ListRoleDto]:
        """List Role Object"""
        raise NotImplementedError

    @abstractmethod
    def get_role(self, role_id: int) -> Union[GetRoleDto, bool]:
        """Get Role Object"""
        raise NotImplementedError

    @abstractmethod
    def assign_role_to_user(self, model: AssignRoleToUserDto):
        """Assign Role Object to User"""
        raise NotImplementedError


class DefaultRoleManagementService(RoleManagementService):
    repository: RoleRepository

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, model: CreateRoleDto):
        role = Role.objects.get(name=model.name)
        if isinstance(role, (GetRoleDto,)):
            return False
        else:
            self.repository.create_role(model)

    def edit_role(self, role_id: int, model: EditRoleDto):
        result = self.repository.edit_role(role_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_role(self) -> List[ListRoleDto]:
        return self.repository.list_role()

    def get_role(self, role_id: int) -> Union[GetRoleDto, bool]:
        role = self.repository.get_role(role_id)
        if isinstance(role, (GetRoleDto,)):
            return role
        return False

    def assign_role_to_user(self, model: AssignRoleToUserDto):
        result = self.repository.assign_role_to_user(model)
        if isinstance(result, (Exception,)):
            return False
        else:
            return True
