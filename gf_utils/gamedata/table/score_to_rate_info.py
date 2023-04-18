from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ScoreToRateInfoInstance:
    id: str  # '0'
    atk_rate: str  # '5'
    def_rate: str  # '5'
    armor_rate: str  # '5'
    armor_piercing_rate: str  # '5'
    dodge_rate: str  # '5'
    night_view_rate: str  # '5'


class ScoreToRateInfo(ConfigTable):
    name = "score_to_rate_info"

    def add_instance(self, k):
        return ScoreToRateInfoInstance(**self._data[k])
