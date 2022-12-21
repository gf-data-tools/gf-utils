
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class AutoMissionInstance:
    mission_id:int # 1
    team_effect:int # 8500
    month_team_count:int # 1
    team_count:int # 1
    mp:int # 210
    ammo:int # 210
    mre:int # 210
    part:int # 70
    duration:int # 3600
    experience:int # 200
    expect_gun_level:int # 100
    get_gun_num:int # 2
    gun_n_pool:str # '9,2,5,10,90,91,92,17,25,93,24,31,33,94,71,68,74,63,51,47,40,41,87,82,11,14,3,12,29,27,58,61,44,37,34,89,1,42,69,75,0'
    gun_1_pool:str # '9,2,5,10,90,91,92,17,25,93,24,31,33,94,71,68,74,63,51,47,40,41,87,82,11,14,3,12,29,27,58,61,44,37,34,89,1,42,69,75'
    limit_guns:str # ''
    get_equip_num:int # 0
    equip_n_pool:str # '0'
    equip_1_pool:str # '0'
    limit_equips:str # ''
    draw_event_id:int # 0

class AutoMission(ConfigTable):
    name = 'auto_mission'

    def add_instance(self,k):
        return AutoMissionInstance(**self._data[k])    
