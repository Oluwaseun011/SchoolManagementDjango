from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.models import Term
from app.dto.term_dto import *
from app.repositories.term_repository import TermRepository, DjangoORMTermRepository


class TermManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_term(self, model: CreateTermDto):
        """Create Term Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_term(self, term_id: int, model: EditTermDto):
        """Edit Term Object"""
        raise NotImplementedError

    @abstractmethod
    def list_term(self) -> List[ListTermDto]:
        """List Term Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_term(self, term_id: int) -> Union[GetTermDto, bool]:
        """Get Term Object"""
        raise NotImplementedError


class DefaultTermManagementService(TermManagementService):
    repository: TermRepository

    def __init__(self, repository: TermRepository):
        self.repository = repository

    def create_term(self, model: CreateTermDto):
        return self.repository.create_term(model)

    def edit_term(self, term_id: int, model: EditTermDto):
        result = self.repository.edit_term(term_id, model)
        if isinstance(result, (Exception,)):
            return False
        else:
            return True

    def list_term(self) -> List[ListTermDto]:
        return self.repository.list_term()

    def get_term(self, term_id: int) -> Union[GetTermDto, bool]:
        result = self.repository.get_term(term_id)
        if isinstance(result, (GetTermDto,)):
            return result
        else:
            return False
