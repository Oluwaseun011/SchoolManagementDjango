from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.dto.subject_dto import *
from app.models import Subject
from app.repositories.subject_repository import SubjectRepository, DjangoORMSubjectRepository


class SubjectManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_subject(self, model: CreateSubjectDto):
        """Create Subject Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_subject(self, subject_id: int, model: EditSubjectDto):
        """Edit Subject Object"""
        raise NotImplementedError

    @abstractmethod
    def list_subjects(self) -> List[ListSubjectDto]:
        """List Subject Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_subject(self, subject_id: int) -> Union[GetSubjectDto, bool]:
        """Get Subject Object"""
        raise NotImplementedError

class DefaultSubjectManagementService(SubjectManagementService):
    repository: SubjectRepository

    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def create_subject(self, model: CreateSubjectDto):
        subject = Subject.objects.get(subject_name=model.subject_name)
        if isinstance(subject, (GetSubjectDto,)):
            return False
        else:
            return self.repository.create_subject(model)

    def edit_subject(self, subject_id: int, model: EditSubjectDto):
        result = self.repository.edit_subject(subject_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_subjects(self) -> List[ListSubjectDto]:
        return self.repository.list_subjects()

    def get_subject(self, subject_id: int) -> Union[GetSubjectDto, bool]:
        result = self.repository.get_subject(subject_id)
        if isinstance(result, (GetSubjectDto,)):
            return result
        else:
            return False

