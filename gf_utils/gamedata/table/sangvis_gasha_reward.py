from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SangvisGashaRewardInstance:
    id: int  # 1001
    sangvis_id: str  # '1001'
    reward_type: int  # 1
    single_num_weight: str  # ''


class SangvisGashaReward(ConfigTable):
    name = "sangvis_gasha_reward"

    def add_instance(self, k):
        return SangvisGashaRewardInstance(**self._data[k])
