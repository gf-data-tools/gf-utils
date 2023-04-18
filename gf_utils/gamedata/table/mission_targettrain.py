from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MissionTargettrainInstance:
    id: int  # 170101
    target_type: int  # 1
    name: str  # '定制标靶'
    target_des: str  # '【为了让各位指挥官对战斗有更深刻的理解，格里芬研发了模拟标靶系统。\\n 您可以在系统中配置有针对性的假想敌，并配置自己的梯队参与模拟作 战。】'
    code: str  # 'mission_targettrain_01'
    rank: int  # 0
    rank_type: int  # 0
    rank_inorder: int  # 0
    hit_rank: int  # 0
    hit_rank_type: int  # 0
    hit_rank_inorder: int  # 0
    difficult_level_limit: int  # 5
    difficult_level: int  # 1
    recommend_level: int  # 20
    target_id: str  # '101'
    battle_timelimit: int  # 300
    hp_is_re: int  # 1
    is_time_limit: int  # 0
    start_time: str  # ''
    end_time: str  # ''
    cost_type: int  # 0
    cost_item: str  # ''
    mp: int  # 0
    ammo: int  # 0
    mre: int  # 0
    part: int  # 0
    is_reward: int  # 0
    prize_reward: str  # ''


class MissionTargettrain(ConfigTable):
    name = "mission_targettrain"

    def add_instance(self, k):
        return MissionTargettrainInstance(**self._data[k])
