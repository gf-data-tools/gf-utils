from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CoffeeshopPvInstance:
    id: str  # '1'
    title: str  # '魔方行动'
    description: str  # '2016年夏季活动视频'
    cost: str  # '506-1000'
    prize_id: str  # '5001'
    item_ids: str  # '0'


class CoffeeshopPv(ConfigTable):
    name = "coffeeshop_pv"

    def add_instance(self, k):
        return CoffeeshopPvInstance(**self._data[k])
