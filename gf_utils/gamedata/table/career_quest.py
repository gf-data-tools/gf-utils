from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class CareerQuestInstance:
    id: int  # 1
    type: str  # 'auto_mission_1'
    unlock_lv: str  # ''
    unlock_ids: str  # ''
    unlock_label: str  # ''
    count: int  # 1
    prize_id: int  # 701
    title: str  # '战役任务：自律作战'
    content: str  # '完成1次1-1自律作战（注：自律作战可以让小队自动进行战斗。完成战斗获得人形或装备。获得关卡3枚勋章可开启该关卡自律作战）'
    unlock_course: str  # ''
    new_type: int  # 1
    grade_id: int  # 47
    sort: int  # 359
    condition: str  # ''
    new_unlock_ids: str  # ''


class CareerQuest(ConfigTable):
    name = "career_quest"

    def add_instance(self, k):
        return CareerQuestInstance(**self._data[k])
