from abc import ABCMeta, abstractmethod
from typing import List, Union
from app.models import Application
from app.dto.application_dto import *
from app.repositories.application_repository import ApplicationRepository


class ApplicationManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_application(self, model: CreateApplicationDto):
        """Create Application Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_application(self, application_id: int, model: EditApplicationDto):
        """Edit Application Object"""
        raise NotImplementedError

    @abstractmethod
    def list_applications(self) -> List[ListApplicationDto]:
        """List Applications Object"""
        raise NotImplementedError

    @abstractmethod
    def get_application(self, application_id=None, email=None) -> Union[GetApplicationDto, bool]:
        """Application Object Details"""
        raise NotImplementedError

    @abstractmethod
    def activate_application(self, application_id: int, model: ActivateApplicationDto):
        """Activate Application Object"""
        raise NotImplementedError


class DefaultApplicationManagementService(ApplicationManagementService):
    repository: ApplicationRepository

    def __init__(self, repository: ApplicationRepository):
        self.repository = repository

    def create_application(self, model: CreateApplicationDto):
        return self.repository.create_application(model)

    def edit_application(self, application_id: int, model: EditApplicationDto):
        result = self.repository.edit_application(application_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_applications(self) -> List[ListApplicationDto]:
        return self.repository.list_applications()

    def get_application(self, application_id=None, email=None) -> Union[GetApplicationDto, bool]:
        result = self.repository.get_application(application_id=application_id, email=email)
        if isinstance(result, (GetApplicationDto,)):
            return result
        else:
            return False

    def activate_application(self, application_id: int, model: ActivateApplicationDto):
        application = self.repository.activate_application(application_id, model)
        if isinstance(application, (Exception,)):
            return False
        return True
