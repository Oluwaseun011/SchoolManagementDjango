from abc import abstractmethod, ABCMeta

import uuid

from app.models import Basic
from app.dto.basic_dto import *
from app.dto.common_dto import *
from typing import List, Union


class BasicRepository(metaclass=ABCMeta):
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


class DjangoORMBasicRepository(BasicRepository):
    def create_basic(self, model: CreateBasicDto):
        basic = Basic()
        basic.id = uuid.uuid4()
        basic.basic_name = model.basic_name
        basic.save()

    def edit_basic(self, basic_id: int, model: EditBasicDto):
        try:
            basic = Basic.objects.get(id=basic_id)
            basic.basic_name = model.basic_name
            basic.save()
        except Basic.DoesNotExist as e:
            return e

    def list_basic(self) -> List[ListBasicDto]:
        basics = Basic.objects.all()
        result: List[ListBasicDto] = []
        for basic in basics:
            item = ListBasicDto()
            item.basic_name = basic.basic_name
            result.append(item)
        return result

    def get_basic(self, basic_id=None, basic_name=None) -> Union[GetBasicDto, bool]:
        try:
            if basic_id is not None:
                basic = Basic.objects.get(id=basic_id)
            elif basic_name is not None:
                basic = Basic.objects.get(basic_name=basic_name)
            item = GetBasicDto()
            item.id = basic.id
            item.basic_name = basic.basic_name
            return item
        except Basic.DoesNotExist as e:
            return e

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        basic = Basic.objects.values("id", "basic_name")
        return [SelectOptionDto(a["id"], a["basic_name"]) for a in basic]
