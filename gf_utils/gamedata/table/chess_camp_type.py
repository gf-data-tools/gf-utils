from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessCampTypeInstance:
    id: int  # 1
    name: str  # 'I.O.P科技'
    des: str  # '一家三战期间成立的工业制造公司，战争期间获得了前90wish帕斯卡的技术支持，开始生产战术人形。'
    camp_skill: str  # '303'
    passive_skill: str  # '30320,30321'
    color: str  # '#C7E001FF'
    code: str  # 'MiniGameFlightChessCamp1'


class ChessCampType(ConfigTable):
    name = "chess_camp_type"

    def add_instance(self, k):
        return ChessCampTypeInstance(**self._data[k])
