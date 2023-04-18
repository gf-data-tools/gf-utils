from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MissionBuffConfigInstance:
    id: int  # 1
    name: str  # '减耗BUFF'
    description: str  # '一定回合数消耗为零'
    code: str  # 'buff'
    type: int  # 1
    duration_type: str  # '1'
    duration_time: str  # '3'
    limit_buff: str  # '0'
    exp_buff: str  # '1'
    is_resource_buff: int  # 3
    vision_buff: str  # '0'
    cannot_move: str  # ''
    battle_skill_config_id: int  # 0
    property_type: str  # '0'
    property_data_pool: str  # '0'
    special_spot_config_id: int  # 0
    conditions_type: str  # '0'
    conditions_time: str  # '0'
    birth_effect: int  # 0
    effect_process_star: int  # 0
    effect_process_end: int  # 0
    effect_process_duration: int  # 0
    manual_ui_code: str  # ''
    ammo_mre_reduce: str  # ''
    free_ap_move: int  # 0
    extra_ammo_mre: str  # ''
    conflict_type: int  # 1
    priority: int  # 0
    carry_mission_skill: str  # ''
    sangvis_chip_id: str  # ''
    ext_move: int  # 0


class MissionBuffConfig(ConfigTable):
    name = "mission_buff_config"

    def add_instance(self, k):
        return MissionBuffConfigInstance(**self._data[k])
