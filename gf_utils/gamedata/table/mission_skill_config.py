
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionSkillConfigInstance:
    id:int # 101
    name:str # 'surprise_mother_fuck'
    code:str # 'No_consumption'
    description:str # 'surprise_mother_fuck'
    lvup_description:str # 'surprise_mother_fuck'
    skill_group_id:int # 1
    level:int # 1
    train_coin_type:int # 0
    train_coin_number:int # 0
    skill_up_time:int # 0
    spot_type:str # '-1'
    spot_belong:str # '-1'
    spot_echelon:str # '-1'
    cd_time:int # 1
    cd_time_type:int # 0
    consumption:int # 20
    start_range:int # 0
    is_night:int # 0
    data_pool:str # '1'
    is_airborne:int # 0
    airborne_mission_buff_config_id:int # 0
    effect_cast:str # '0'
    effect_self:str # '0'
    effect_target:str # '0'
    trigger_id:str # ''
    target_id:str # ''
    special_spot_add:str # '1:1'
    special_spot_minus:str # ''
    mission_buff_add:str # ''
    mission_buff_minus:str # ''
    subsidiary_mission_skill:str # ''
    is_manual:int # 0
    allyteam_summoner:str # ''
    ap_cost:int # 0
    consumption_item:str # ''
    drop_item:str # ''
    fun_game_type:int # 0
    fun_game_name:str # ''
    fun_game_result_sub:str # ''

class MissionSkillConfig(ConfigTable):
    name = 'mission_skill_config'

    def add_instance(self,k):
        return MissionSkillConfigInstance(**self._data[k])    
