from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class CommanderRankingTypesInstance:
    id: int  # 201
    class_id: int  # 2
    title: str  # '战术人形等级'
    desc: str  # 'commander_ranking_types-20000201'
    weight: float  # 0.01
    page_to_go: int  # 0


class CommanderRankingTypes(ConfigTable):
    name = "commander_ranking_types"

    def add_instance(self, k):
        return CommanderRankingTypesInstance(**self._data[k])
