from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class DailyInstance:
    identity: int  # 1
    mission_type: int  # 1
    type: str  # 'win_normal'
    count: int  # 50
    user_exp: int  # 0
    mp: int  # 0
    ammo: int  # 0
    mre: int  # 0
    part: int  # 0
    core: int  # 0
    gem: int  # 0
    gun_id: int  # 0
    item_ids: str  # ''
    title: str  # '战斗：作战行动'
    content: str  # '战斗胜利情况下消灭50个普通单位。'
    function_control_id: int  # 0
    prize_id: int  # 8308
    exchange_prize_id: int  # 8315


class Daily(ConfigTable):
    name = "daily"

    def add_instance(self, k):
        return DailyInstance(**self._data[k])
