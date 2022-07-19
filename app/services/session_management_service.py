from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.models import Session
from app.dto.session_dto import *
from app.repositories.session_repository import SessionRepository, DjangoORMSessionRepository


class SessionManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_session(self, model: CreateSessionDto):
        """Create Session Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_session(self, session_id: int, model: EditSessionDto):
        """Edit Session Object"""
        raise NotImplementedError

    @abstractmethod
    def list_session(self) -> List[ListSessionDto]:
        """List Session Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_session(self, session_id: int) -> Union[GetSessionDto, bool]:
        """Get Session Object"""
        raise NotImplementedError


class DefaultSessionManagementService(SessionManagementService):
    repository: SessionRepository

    def __init__(self, repository: SessionRepository):
        self.repository = repository

    def create_session(self, model: CreateSessionDto):
        session = Session.objects.get(session_name=model.session_name)
        if isinstance(session, (GetSessionDto,)):
            return False
        else:
            return self.repository.create_session(model)

    def edit_session(self, session_id: int, model: EditSessionDto):
        result = self.repository.edit_session(session_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_session(self) -> List[ListSessionDto]:
        return self.repository.list_session()

    def get_session(self, session_id: int) -> Union[GetSessionDto, bool]:
        result = self.repository.get_session(session_id)
        if isinstance(result, (GetSessionDto,)):
            return result
        else:
            return False
