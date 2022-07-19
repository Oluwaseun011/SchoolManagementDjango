from abc import abstractmethod, ABCMeta
from app.models import Student, Person
from app.dto.student_dto import *
from typing import List, Union


class StudentRepository(metaclass=ABCMeta):
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


class DjangoORMStudentRepository(StudentRepository):
    def register_student(self, model: RegisterStudentDto):
        student = Student()
        student.id = model.id
        student.person_id = model.person_id
        student.admin_number = model.admin_number
        student.admin_year = model.admin_year
        student.save()

    def edit_student(self, student_id: int, model: EditStudentDto):
        student = Student.objects.get(id=student_id)
        student.admin_number = model.admin_number
        student.save()

    def list_students(self) -> List[ListStudentDto]:
        students = Student.objects.all()
        result: List[ListStudentDto] = []
        for student in students:
            item = ListStudentDto()
            item.student_name = student.person.first_name + " " + student.person.last_name
            item.admin_number = student.admin_number
            item.basic = student.basic.basic_name
            result.append(item)
        return result

    def get_student(self, student_id=None, person_id=None) -> Union[GetStudentDto, bool]:
        try:
            if student_id is not None:
                student = Student.objects.get(id=student_id)
            elif person_id is not None:
                student = Student.objects.get(id=person_id)
            item = GetStudentDto()
            item.id = student.id
            item.admin_number = student.person_id
            item.admin_number = student.admin_number
            return item
        except Student.DoesNotExist as e:
            return e
