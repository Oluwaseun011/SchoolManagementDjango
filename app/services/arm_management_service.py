from abc import abstractmethod, ABCMeta
from app.models import Arm
from app.dto.arm_dto import *
from typing import List, Union
from app.repositories.arm_repository import ArmRepository, DjangoORMArmRepository


class ArmManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_arm(self, model: CreateArmDto):
        """Create Arm Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_arm(self, arm_id: int, model: EditArmDto):
        """Edit Arm Object"""
        raise NotImplementedError

    @abstractmethod
    def list_arm(self) -> List[ListArmDto]:
        """List Arms Object"""
        raise NotImplementedError

    @abstractmethod
    def get_arm(self, arm_id: int) -> Union[GetArmDto, bool]:
        """Get Arm Object"""
        raise NotImplementedError


class DefaultArmManagementService(ArmManagementService):
    repository: ArmRepository

    def __init__(self, repository: ArmRepository):
        self.repository = repository

    def create_arm(self, model: CreateArmDto):
        return self.repository.create_arm(model)

    def edit_arm(self, arm_id: int, model: EditArmDto):
        result = self.repository.edit_arm(arm_id, model)
        if isinstance(result, (Exception,)):
            return False
        return True

    def list_arm(self) -> List[ListArmDto]:
        return self.repository.list_arm()

    def get_arm(self, arm_id: int) -> Union[GetArmDto, bool]:
        result = self.repository.get_arm(arm_id)
        if isinstance(result, (GetArmDto,)):
            return result
        else:
            return False
        


