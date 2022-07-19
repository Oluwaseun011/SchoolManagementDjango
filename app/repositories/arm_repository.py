from abc import abstractmethod, ABCMeta
from app.models import Arm
from app.dto.arm_dto import *
from typing import List, Union


class ArmRepository(metaclass=ABCMeta):
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


class DjangoORMArmRepository(ArmRepository):
    def create_arm(self, model: CreateArmDto):
        arm = Arm()
        arm.id = model.id
        arm.arm_name = model.arm_name
        arm.basic_id = model.basic_id
        arm.save()

    def edit_arm(self, arm_id: int, model: EditArmDto):
        try:
            arm = Arm.objects.get(id=arm_id)
            arm.arm_name = model.arm_name
            arm.save()
        except Arm.DoesNotExist as e:
            return e

    def list_arm(self) -> List[ListArmDto]:
        arms = Arm.objects.all()
        result: List[ListArmDto] = []

        for arm in arms:
            item = ListArmDto()
            item.arm_name = arm.arm_name
            item.basic_name = arm.basic.basic_name
            result.append(item)
        return result

    def get_arm(self, arm_id: int) -> Union[GetArmDto, bool]:
        try:
            arm = Arm.objects.get(id=arm_id)
            item = GetArmDto()
            item.id = arm.id
            item.arm_name = arm.arm_name
            item.basic_id = arm.basic.id
            return item
        except Arm.DoesNotExist as e:
            return e

        
