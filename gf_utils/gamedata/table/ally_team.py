
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class AllyTeamInstance:
    id:int # 1
    code:str # 'profilePic_AI'
    ui_image_icon:str # 'ally0'
    name:str # '格里芬'
    guns:str # '1,2,3,4,5'
    fairy:int # 0
    enemy_team_id:int # 1486
    initial_type:int # 1
    ai:str # '103;1;103'
    ai_content:str # '0;0;0'
    betray_condition:str # '0'
    betray_number:str # '0'
    betray_result:str # '0'
    transform_condition:str # '0'
    transform_number:str # '0'
    transform_result:str # '0'
    icon:str # ''
    betray_result_enemy:str # ''
    squad:int # 0
    building:int # 0
    enemy_panel_type:int # 1
    is_special_ai:int # 0
    no_battle_damage:int # -1
    duration:int # 0
    sangvis:str # ''
    betray_result_guns:str # ''
    betray_result_sangvis:str # ''

class AllyTeam(ConfigTable):
    name = 'ally_team'

    def add_instance(self,k):
        return AllyTeamInstance(**self._data[k])    
