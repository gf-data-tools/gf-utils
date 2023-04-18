from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChessSkillInstance:
    id: int  # 10101
    cd_type: int  # 1
    init_cd: int  # 0
    cd: int  # 0
    duration: str  # '2:-1'
    trigger: str  # '10102'
    target_buff: str  # '101:1'
    self_buff: str  # '0'
    random_buff: str  # ''
    hurt: str  # '0'
    heal: str  # '0'
    chip: str  # '0'
    dice: str  # '0'
    movement_type: int  # 0
    movement_parameter: int  # 0
    stage_change: str  # '0'
    perform_creation_id: str  # '0'
    effect_range: str  # ''
    summoner: str  # '0'
    token: int  # 0
    negative_skill_target: int  # 6
    chip_ui_control: int  # 3
    score: int  # 0
    flight: int  # 0
    action: str  # ''


class ChessSkill(ConfigTable):
    name = "chess_skill"

    def add_instance(self, k):
        return ChessSkillInstance(**self._data[k])
