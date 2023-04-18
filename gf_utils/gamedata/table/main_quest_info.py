from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MainQuestInfoInstance:
    type: str  # 'medal1-0-1-1'
    count: str  # '1'
    identity: str  # '1'
    user_exp: str  # '10'
    mp: str  # '30'
    ammo: str  # '30'
    mre: str  # '30'
    part: str  # '10'
    core: str  # '0'
    gem: str  # '0'
    gun_id: str  # '29'
    item_ids: str  # ''
    title: str  # '完成行动：普通1-1'
    content: str  # '首次通过普通1-1，获得该关卡铜星勋章。'
    equip_ids: str  # ''
    prize_id: str  # '0'


class MainQuestInfo(ConfigTable):
    name = "main_quest_info"

    def add_instance(self, k):
        return MainQuestInfoInstance(**self._data[k])
