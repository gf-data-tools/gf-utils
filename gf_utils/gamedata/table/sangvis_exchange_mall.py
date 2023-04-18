from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SangvisExchangeMallInstance:
    id: int  # 1
    cost_item: int  # 512
    cost_num: int  # 800
    prize_id: int  # 4213
    quota: int  # 1
    start_time: str  # '2020-03-18 00:00:00'
    end_time: str  # '2020-04-16 10:00:00'


class SangvisExchangeMall(ConfigTable):
    name = "sangvis_exchange_mall"

    def add_instance(self, k):
        return SangvisExchangeMallInstance(**self._data[k])
