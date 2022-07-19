from abc import ABCMeta, abstractmethod
from app.dto.student_dto import *
from app.models import Student
from app.repositories.student_repository import StudentRepository, DjangoORMStudentRepository
from typing import List, Union


class StudentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_student(self, model: RegisterStudentDto):
        """Register Student Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_student(self, student_id: int, model: EditStudentDto):
        """Edit Student Object"""
        raise NotImplementedError

    @abstractmethod
    def list_students(self) -> List[ListStudentDto]:
        """List Student Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_student(self, student_id=None, person_id=None) -> Union[GetStudentDto, bool]:
        """Get Student Object"""
        raise NotImplementedError


class DefaultStudentManagementService(StudentManagementService):
    repository: StudentRepository

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def register_student(self, model: RegisterStudentDto):
        student = Student.objects.get(id=model.id)
        if isinstance(student, (RegisterStudentDto,)):
            return False
        return True

    def edit_student(self, student_id: int, model: EditStudentDto):
        result = self.repository.edit_student(student_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_students(self) -> List[ListStudentDto]:
        return self.repository.list_students()

    def get_student(self, student_id=None, person_id=None) -> Union[GetStudentDto, bool]:
        result = self.repository.get_student(student_id, person_id)
        if isinstance(result, (GetStudentDto,)):
            return result
        else:
            return False
