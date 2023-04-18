from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class BattleWatchInstance:
    id: int  # 1001
    description: str  # '老李增益buff监视1'
    max_times: int  # 0
    if_delete_buff: int  # 0
    record_chara1: int  # 1000004731
    record_chara2: int  # 0
    watch_trigger_type: int  # 1
    watch_sp_trigger: str  # '0'
    activation_watch_trigger: int  # 1001
    activation_skills: str  # '740058'
    sp_skill_target: str  # '0'
    record_watch_trigger: int  # 0
    new_record_chara1: int  # 1000004731
    new_record_chara2: int  # 0
    unactivation_skills: str  # '0'
    sp_unaskill_target: str  # '0'
    ending_watch_trigger: str  # '0'
    ending_activation_skills: str  # '0'
    sp_endingskill_target: str  # '0'


class BattleWatch(ConfigTable):
    name = "battle_watch"

    def add_instance(self, k):
        return BattleWatchInstance(**self._data[k])
