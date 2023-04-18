from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CommanderClassInstance:
    id: int  # 10
    name: str  # '末日迷彩'
    description: str  # '“你一身这么干净是人都知道你偷懒了，来，路边那个泥坑里先打个滚”'
    group_id: str  # '51'
    code: str  # 'commander_10_icon'
    bonus_plastic: str  # ''
    skill_id: int  # 0
    path: str  # 'CLASS10'
    is_class: int  # 1
    des_year: str  # '2019'
    source: int  # 1
    source_description: str  # 'commander_class-40000010'


class CommanderClass(ConfigTable):
    name = "commander_class"

    def add_instance(self, k):
        return CommanderClassInstance(**self._data[k])
