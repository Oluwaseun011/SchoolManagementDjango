from abc import abstractmethod, ABCMeta
from typing import List, Union
from app.dto.subject_dto import *
from app.models import Subject


class SubjectRepository(metaclass=ABCMeta):
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


class DjangoORMSubjectRepository(SubjectRepository):
    def create_subject(self, model: CreateSubjectDto):
        subject = Subject()
        subject.id = model.id
        subject.subject_name = model.subject_name
        subject.save()

    def edit_subject(self, subject_id: int, model: EditSubjectDto):
        try:
            subject = Subject.objects.get(id=subject_id)
            subject.subject_name = model.subject_name
            subject.save()
        except Subject.DoesNotExist as e:
            return e

    def list_subjects(self) -> List[ListSubjectDto]:
        subjects = Subject.objects.all()
        result: List[ListSubjectDto] = []
        for subject in subjects:
            item = ListSubjectDto()
            item.subject_name = subject.subject_name
            result.append(item)
        return result

    def get_subject(self, subject_id: int) -> Union[GetSubjectDto, bool]:
        try:
            subject = Subject.objects.get(id=subject_id)
            item = GetSubjectDto()
            item.id = subject.id
            item.subject_name = subject.subject_name
            return item
        except Subject.DoesNotExist as e:
            return e
        




