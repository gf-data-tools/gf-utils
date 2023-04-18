from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class WeeklyInstance:
    identity: int  # 1
    type: str  # 'battery_collect'
    count: int  # 3
    user_exp: int  # 0
    mp: int  # 0
    ammo: int  # 0
    mre: int  # 0
    part: int  # 0
    core: int  # 0
    gem: int  # 0
    gun_id: int  # 0
    item_ids: str  # ''
    title: str  # '每周要务：电力采集'
    content: str  # '收取3次宿舍电池。'
    function_control_id: int  # 0
    prize_id: int  # 8309
    exchange_prize_id: int  # 8316


class Weekly(ConfigTable):
    name = "weekly"

    def add_instance(self, k):
        return WeeklyInstance(**self._data[k])
