
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SpecialSpotConfigInstance:
    id:int # 1
    name:str # '减耗BUFF点'
    description:str # '减耗妖精生成的初期特殊点，出生时给我方梯队释放BUFF'
    code:str # '1'
    priority:int # 9
    duration_type:str # '1'
    duration_time:str # '0'
    special_spot_config_id:int # 0
    mission_hurt_config_id:int # 0
    mission_buff_config_id:int # 0
    detect_target_type:str # '1'
    detect_range:int # 0
    effect_target_type:str # '0'
    effect_spotbelong_type:str # '0,1,2,3'
    effect_range_type:int # 1
    effect_range:int # 0
    side_type:int # 0
    conflict_type:int # 1
    conditions_type:str # '0;0'
    conditions_time:str # '0-0;0-0'
    conditions_count:int # 0
    skill_config_id_on_birth:str # '1,0,0'
    skill_config_id_on_death:str # '0,0,0'
    death_effect_target_type:str # '0'
    death_clear_spot:str # '0'
    effect_birth:int # 0
    effect_death:int # 0
    effect_duration:int # 0
    effect_process_star:int # 0
    effect_process_end:int # 0
    effect_process_duration:int # 0
    effect_conditions:str # '0,1'
    effect_conditions_type:str # '0'
    spot_buff_config_id:int # 0
    pref_code:str # ''
    is_still_alive:int # 0

class SpecialSpotConfig(ConfigTable):
    name = 'special_spot_config'

    def add_instance(self,k):
        return SpecialSpotConfigInstance(**self._data[k])    
