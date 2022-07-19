from abc import ABCMeta, abstractmethod
from typing import List, Union

from app.dto.common_dto import SelectOptionDto
from app.models import Basic
from app.dto.basic_dto import *
from app.repositories.basic_repository import BasicRepository, DjangoORMBasicRepository


class BasicManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_basic(self, model: CreateBasicDto):
        """Create Basic Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_basic(self, basic_id: int, model: EditBasicDto):
        """Edit Basic Object"""
        raise NotImplementedError

    @abstractmethod
    def list_basic(self) -> List[ListBasicDto]:
        """List Basics Object"""
        raise NotImplementedError

    @abstractmethod
    def get_basic(self, basic_id=None, basic_name=None) -> Union[GetBasicDto, bool]:
        """Get Basic Object"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a basic object"""
        raise NotImplementedError


class DefaultBasicManagementService(BasicManagementService):
    repository: BasicRepository

    def __init__(self, repository: BasicRepository):
        self.repository = repository

    def create_basic(self, model: CreateBasicDto):
        basic = self.repository.get_basic(basic_name=model.basic_name)
        if isinstance(basic, (GetBasicDto,)):
            return False
        else:
            return self.repository.create_basic(model)

    def edit_basic(self, basic_id: int, model: EditBasicDto):
        result = self.repository.edit_basic(basic_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_basic(self) -> List[ListBasicDto]:
        return self.repository.list_basic()

    def get_basic(self, basic_id=None, basic_name=None) -> Union[GetBasicDto, bool]:
        result = self.repository.get_basic(basic_id)
        if isinstance(result, (GetBasicDto,)):
            return result
        else:
            return False

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()
