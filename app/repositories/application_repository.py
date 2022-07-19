from abc import ABCMeta, abstractmethod
from typing import List, Union

import uuid

from app.models import Application
from app.dto.application_dto import *


class ApplicationRepository(metaclass=ABCMeta):
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


class DjangoORMApplicationRepository(ApplicationRepository):
    def create_application(self, model: CreateApplicationDto):
        application = Application()
        application.id = uuid.uuid4()
        application.basic_id = model.basic_id
        application.application_score = model.application_no
        application.email = model.email
        application.first_name = model.first_name
        application.last_name = model.last_name
        application.status = model.status
        application.application_score = model.application_score
        application.passport = model.passport
        application.save()

    def edit_application(self, application_id: int, model: EditApplicationDto):
        try:
            application = Application.objects.get(id=application_id)
            application.email = model.email
            application.first_name = model.first_name
            application.last_name = model.last_name
            application.save()
        except Application.DoesNotExist as e:
            return e

    def list_applications(self) -> List[ListApplicationDto]:
        applications = Application.objects.all()
        results: List[ListApplicationDto] = []

        for application in applications:
            item = ListApplicationDto()
            item.applicants = application.first_name + " " + application.last_name
            item.status = application.status
            results.append(item)
        return results

    def get_application(self, application_id=None, email=None) -> Union[GetApplicationDto, bool]:
        try:
            if application_id is not None:
                application = Application.objects.get(id=application_id)
            elif email is not None:
                application = Application.objects.get(email=email)
            item = GetApplicationDto()
            item.id = application.id
            item.email = application.email
            item.first_name = application.first_name
            item.last_name = application.last_name
            item.status = application.status
            return item
        except Application.DoesNotExist as e:
            return e

    def activate_application(self, application_id: int, model: ActivateApplicationDto):
        try:
            application = Application.objects.get(id=application_id)
            application.status = model.status
            application.save()
        except Application.DoesNotExist as e:
            return e
