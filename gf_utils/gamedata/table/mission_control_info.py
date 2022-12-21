
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionControlInfoInstance:
    id:str # '1'
    turn_code:str # 'GKLOGO'
    turn_color:str # '#76980047'
    spot_color:str # '#96C8FAFF'
    team_code:str # 'Friend'
    team_color:str # '#96C8FA96'
    team_ai_color:str # '#96C8FAFF'
    blood_color:str # '#6FDDCBFF'

class MissionControlInfo(ConfigTable):
    name = 'mission_control_info'

    def add_instance(self,k):
        return MissionControlInfoInstance(**self._data[k])    
