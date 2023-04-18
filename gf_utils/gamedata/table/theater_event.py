from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TheaterEventInstance:
    id: int  # 4
    name: str  # '战区攻略测试'
    start_time: str  # '2019-07-04 00:04:00'
    end_time: str  # '2019-07-25 10:30:00'
    close_time: str  # '2019-08-08 00:04:00'
    banner: int  # 0
    primary_theater: str  # '41,42,43'
    core_theater: int  # 44
    ap_recover: int  # 2
    opening_time: str  # '5,4'
    pt_gift: str  # '3000:44001,15000:44002,35000:44003,55000:44004,75000:44005,100000:44006,130000:44007,160000:44008,190000:44009,220000:44010,250000:44011'
    background: str  # 'TheaterBackground'
    gift_background: str  # 'carnival_20180816.png'
    gift_figure: str  # 'pic_AA12.png'


class TheaterEvent(ConfigTable):
    name = "theater_event"

    def add_instance(self, k):
        return TheaterEventInstance(**self._data[k])
