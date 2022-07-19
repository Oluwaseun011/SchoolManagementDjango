from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.models import Term
from app.dto.term_dto import *


class TermRepository(metaclass=ABCMeta):
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


class DjangoORMTermRepository(TermRepository):
    def create_term(self, model: CreateTermDto):
        term = Term()
        term.id = model.id
        term.term_name = model.term_name
        term.session_id = model.session_id
        term.term_status = model.term_status
        term.save()

    def edit_term(self, term_id: int, model: EditTermDto):
        try:
            term = Term.objects.get(id=term_id)
            term.term_name = model.term_name
            term.save()
        except Term.DoesNotExist as e:
            return e

    def list_term(self) -> List[ListTermDto]:
        terms = Term.objects.all()
        result: List[ListTermDto] = []
        for term in terms:
            item = ListTermDto()
            item.term_name = term.term_name
            item.session_name = term.session.session_name
            item.term_status = term.term_status
            result.append(item)
        return result

    def get_term(self, term_id: int) -> Union[GetTermDto, bool]:
        try:
            term = Term.objects.get(id=term_id)
            item = GetTermDto()
            item.id = term.id
            item.session_id = term.session_id
            item.term_name = term.term_name
            item.term_status = term.term_status
            return item
        except Term.DoesNotExist as e:
            return e
