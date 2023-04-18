from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SangvisGashaInstance:
    id: int  # 0
    name: str  # '斯氏联合基地'
    type: int  # 1
    start_time: str  # '2019-04-01 00:00:00'
    end_time: str  # '2037-12-01 00:00:00'
    tab_code: str  # 'banner_collection57_s.jpg'
    banner: str  # 'banner_collection57_s.jpg'
    refresh_rate: int  # 259200
    daily_price: str  # '604:1'
    author_price: str  # '605:1'
    gasha_reward_ids: str  # '1001:1,3002:9,3003:9,3004:10,5005:10,5006:10,5007:10,5008:10,5009:10,5010:10,5011:11'


class SangvisGasha(ConfigTable):
    name = "sangvis_gasha"

    def add_instance(self, k):
        return SangvisGashaInstance(**self._data[k])
