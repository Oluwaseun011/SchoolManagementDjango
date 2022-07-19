from abc import abstractmethod, ABCMeta
from app.dto.person_dto import *
from app.models import Person
from typing import List, Union


class PersonRepository(metaclass=ABCMeta):
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


class DjangoORMPersonRepository(PersonRepository):
    def create_person(self, model: CreatePersonDto):
        person = Person()
        person.id = model.id
        person.first_name = model.first_name
        person.last_name = model.last_name
        person.email = model.email
        person.password = model.password
        person.address = model.address
        person.gender = model.gender
        person.telephone = model.telephone
        person.date_of_birth = model.date_of_birth
        person.save()

    def edit_person(self, person_id: int, model: EditPersonDto):
        try:
            person = Person.objects.get(id=person_id)
            person.first_name = model.first_name
            person.last_name = model.last_name
            person.email = model.email
            person.address = model.address
            person.gender = model.gender
            person.telephone = model.telephone
            person.date_of_birth = model.date_of_birth
            person.save()
        except Person.DoesNotExist as e:
            return e

    def list_person(self) -> List[ListPersonDto]:
        persons = Person.objects.all()
        result: List[ListPersonDto] = []
        for person in persons:
            item = ListPersonDto()
            item.name = person.first_name + " " + person.last_name
            item.gender = person.gender
            result.append(item)
        return result

    def get_person(self, person_id=None, email=None) -> Union[GetPersonDto, bool]:
        try:
            if person_id is not None:
                person = Person.objects.get(id=person_id)
            elif email is not None:
                person = Person.objects.get(email=email)
            item = GetPersonDto()
            item.id = person.id
            item.first_name = person.last_name
            item.last_name = person.last_name
            item.email = person.email
            item.gender = person.gender
            item.address = person.address
            item.telephone = person.telephone
            item.date_of_birth = person.date_of_birth
            return item
        except Person.DoesNotExist as e:
            return e

    def authenticate(self, model: AuthenticateDto) -> bool:
        person = Person.objects.filter(email=model.email, password=model.password).exists()
        return person

    def change_password(self, person_id: int, model: ChangePasswordDto):
        try:
            person = Person.objects.get(id=person_id)
            person.password = model.new_password
            person.save()
        except Person.DoesNotExist as e:
            return e
