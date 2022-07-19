from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.models import Session
from app.dto.session_dto import *


class SessionRepository(metaclass=ABCMeta):
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

class DjangoORMSessionRepository(SessionRepository):
    def create_session(self, model: CreateSessionDto):
        session = Session()
        session.session_name = model.session_name
        session.session_start = model.session_start
        session.session_end = model.session_end
        session.session_status = model.session_status
        session.save()

    def edit_session(self, session_id: int, model: EditSessionDto):
        try:
            session = Session.objects.get(id=session_id)
            session.session_name = model.session_name
            session.session_start = model.session_start
            session.session_end = model.session_end
            session.save()
        except Session.DoesNotExist as e:
            raise e

    def list_session(self) -> List[ListSessionDto]:
        sessions = Session.objects.all()
        result: List[ListSessionDto] = []
        for session in sessions:
            item = ListSessionDto()
            item.session_name = session.session_name
            item.session_status = session.session_status
            result.append(item)
        return result

    def get_session(self, session_id: int) -> Union[GetSessionDto, bool]:
        try:
            session = Session.objects.get(id=session_id)
            item = GetSessionDto()
            item.id = session.id
            item.session_name = session.session_name
            item.session_start = session.session_start
            item.session_end = session.session_end
            item.session_status = session.session_status
            return item
        except Session.DoesNotExist as e:
            return e
