class CreateArmDto:
    id: int
    basic_id: int
    arm_name: str


class EditArmDto:
    id: int
    arm_name: str


class ListArmDto:
    basic_name: int
    arm_name: str


class GetArmDto:
    id: int
    basic_id: int
    arm_name: str
