from abc import ABCMeta, abstractmethod
from typing import List, Union
from app.models import Employee
from app.dto.employee_dto import *
from app.repositories.employee_repository import EmployeeRepository, DjangoORMEmployeeRepository


class EmployeeManagementService(metaclass=ABCMeta):
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


class DefaultEmployeeManagementService(EmployeeManagementService):
    repository: EmployeeRepository

    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def create_employee(self, model: CreateEmployeeDto):
        employee = Employee.objects.get(model.person_id)
        if isinstance(employee, (GetEmployeeDto,)):
            return False
        else:
            return self.repository.create_employee(model)

    def edit_employee(self, employee_id: int, model: EditEmployeeDto):
        result = self.repository.edit_employee(employee_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_employee(self) -> List[ListEmployeeDto]:
        return self.repository.list_employee()

    def get_employee(self, employee_id: int) -> Union[GetEmployeeDto, bool]:
        employee = self.repository.get_employee(employee_id)
        if isinstance(employee, (GetEmployeeDto,)):
            return employee
        else:
            return False



