from abc import abstractmethod, ABCMeta
from app.models import Role, Person
from app.dto.role_dto import *
from typing import List, Union


class RoleRepository(metaclass=ABCMeta):
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


class DjangoORMRoleRepository(RoleRepository):
    def create_role(self, model: CreateRoleDto):
        role = Role()
        role.id = model.id
        role.name = model.name
        role.description = model.description
        role.save()

    def edit_role(self, role_id: int, model: EditRoleDto):
        try:
            role = Role.objects.get(id=role_id)
            role.name = model.name
            role.description = model.description
            role.save()
        except Role.DoesNotExist as e:
            return e

    def list_role(self) -> List[ListRoleDto]:
        roles = Role.objects.all()
        result: List[ListRoleDto] = []

        for role in roles:
            item = ListRoleDto()
            item.name = role.name
            result.append(item)
        return result

    def get_role(self, role_id: int) -> Union[GetRoleDto, bool]:
        role = Role.objects.get(id=role_id)
        item = GetRoleDto()
        item.id = role.id
        item.name = role.name
        item.description = role.description
        return item

    def assign_role_to_user(self, model: AssignRoleToUserDto):
        try:
            role = Role.objects.get(id=model.role_id)
            Person.objects.get(id=model.person_id).role.add(role)
        except Exception as e:
            return e
