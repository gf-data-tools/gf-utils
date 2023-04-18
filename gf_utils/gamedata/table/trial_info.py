from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TrialInfoInstance:
    id: str  # '1'
    enemy_team_id: str  # '20001'
    enemy_level: str  # '30'
    enemy_type: str  # '2'
    is_night: str  # '0'
    reward_voucher: str  # '0'
    prize_id: str  # '0'


class TrialInfo(ConfigTable):
    name = "trial_info"

    def add_instance(self, k):
        return TrialInfoInstance(**self._data[k])
