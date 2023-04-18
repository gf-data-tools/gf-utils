from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionEventPrizeInfoInstance:
    mission_id: str  # '10001'
    boss_hp_bars: str  # '1'
    user_exp: str  # '0'
    mp: str  # '0'
    ammo: str  # '0'
    mre: str  # '0'
    part: str  # '0'
    core: str  # '0'
    gem: str  # '0'
    gun_id: str  # '0'
    item_ids: str  # ''
    equip_ids: str  # ''
    furniture: str  # ''
    gift: str  # ''
    coins: str  # ''
    prize_id: str  # '6001'


class MissionEventPrizeInfo(ConfigTable):
    name = "mission_event_prize_info"

    def add_instance(self, k):
        return MissionEventPrizeInfoInstance(**self._data[k])
