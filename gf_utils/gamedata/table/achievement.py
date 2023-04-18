from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class AchievementInstance:
    identity: int = 1
    type: str = "different_gun"
    count: int = 10
    user_exp: int = 100
    mp: int = 30
    ammo: int = 30
    mre: int = 30
    part: int = 30
    core: int = 1
    gem: int = 0
    gun_id: int = 0
    item_ids: str = "1-1"
    equip_ids: str = ""
    furniture: str = ""
    gift: str = ""
    title: str = "小小兴趣"
    content: str = "图鉴解锁10位不同的战术少女。"
    type_sort: int = 2
    sort: int = 22
    icon_code: str = "获得N把不同枪支"
    prize_id: int = 0
    mission_id: str = ""
    condition: str = ""
    commander_title: str = "achievement-30000001"
    unlock_function: int = 0


class Achievement(ConfigTable):
    name = "achievement"

    def add_instance(self, k):
        return AchievementInstance(**self._data[k])
