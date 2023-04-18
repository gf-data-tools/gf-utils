from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CommanderRankingScoresInstance:
    id: int  # 1
    code: str  # 'sr_gun_level'
    type_id: int  # 201
    basic_scores: float  # 0.7
    k_slopes: str  # '0.5;4.5;2;13;5'
    x_counts: str  # '0;90;100;110;115'


class CommanderRankingScores(ConfigTable):
    name = "commander_ranking_scores"

    def add_instance(self, k):
        return CommanderRankingScoresInstance(**self._data[k])
