from abc import ABCMeta, abstractmethod
from typing import List, Union
from app.repositories.person_repository import PersonRepository, DjangoORMPersonRepository
from app.models import Person
from app.dto.person_dto import *


class PersonManagementService(metaclass=ABCMeta):

    @abstractmethod
    def create_person(self, model: CreatePersonDto):
        """Create Person Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_person(self, person_id: int, model: EditPersonDto):
        """Edit person Object"""
        raise NotImplementedError

    @abstractmethod
    def list_person(self) -> List[ListPersonDto]:
        """List Person Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_person(self, person_id=None, email=None) -> Union[GetPersonDto, bool]:
        """Get Person Object"""
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, model: AuthenticateDto) -> bool:
        """Check Person Object in the Table"""
        raise NotImplementedError

    @abstractmethod
    def change_password(self, person_id: int, model: ChangePasswordDto):
        """Change Object Password"""
        raise NotImplementedError


class DefaultPersonManagementService(PersonManagementService):
    repository: PersonRepository

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def create_person(self, model: CreatePersonDto):
        person = Person.objects.get(email=model.email)
        if isinstance(person, (GetPersonDto,)):
            return False
        else:
            return self.repository.create_person(model)

    def edit_person(self, person_id: int, model: EditPersonDto):
        result = self.repository.edit_person(person_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_person(self) -> List[ListPersonDto]:
        return self.repository.list_person()

    def get_person(self, person_id=None, email=None) -> Union[GetPersonDto, bool]:
        person = self.repository.get_person(person_id, email)
        if isinstance(person, (GetPersonDto,)):
            return person
        else:
            return False

    def authenticate(self, model: AuthenticateDto) -> bool:
        person = self.repository.authenticate(model)
        if isinstance(person, (AuthenticateDto,)):
            return True
        return False

    def change_password(self, person_id: int, model: ChangePasswordDto):
        person = self.repository.change_password(person_id, model)
        if isinstance(person, (Exception,)):
            return False
        return True

