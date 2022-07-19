from abc import ABCMeta, abstractmethod
from typing import List, Union
from app.models import Employee
from app.dto.employee_dto import *


class EmployeeRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_employee(self, model: CreateEmployeeDto):
        """Create Employee Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_employee(self, employee_id: int, model: EditEmployeeDto):
        """Edit Employee Object"""
        raise NotImplementedError

    @abstractmethod
    def list_employee(self) -> List[ListEmployeeDto]:
        """List Employee Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_employee(self, employee_id: int) -> Union[GetEmployeeDto, bool]:
        """Get Employee Object"""
        raise NotImplementedError


class DjangoORMEmployeeRepository(EmployeeRepository):
    def create_employee(self, model: CreateEmployeeDto):
        employee = Employee()
        employee.id = model.id
        employee.person_id = model.person_id
        employee.staff_number = model.staff_number
        employee.employment_status = model.employment_status
        employee.employment_date = model.employment_date
        employee.save()

    def edit_employee(self, employee_id: int, model: EditEmployeeDto):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.staff_number = model.staff_number
            employee.save()
        except Employee.DoesNotExist as e:
            return e

    def list_employee(self) -> List[ListEmployeeDto]:
        employees = Employee.objects.all()
        result: List[ListEmployeeDto] = []
        for employee in employees:
            item = ListEmployeeDto()
            item.employee_name = employee.person.first_name + " " + employee.person.first_name
            item.gender = employee.person.gender
            item.employment_status = employee.employment_status
            result.append(item)
        return result

    def get_employee(self, employee_id: int) -> Union[GetEmployeeDto, bool]:
        employee = Employee.objects.get(id=employee_id)
        item = GetEmployeeDto()
        item.id = employee.id
        item.person_id = employee.person_id
        item.staff_number = employee.staff_number
        item.employment_status = employee.employment_status
        item.employment_date = employee.employment_date
        return item

