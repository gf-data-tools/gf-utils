
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionWinStepControlInstance:
    id:int # 419919
    win_step:str # '3'
    lose_step:str # ''
    next_id:str # 'win0'
    lock_id:str # ''
    related_missionkey:str # ''

class MissionWinStepControl(ConfigTable):
    name = 'mission_win_step_control'

    def add_instance(self,k):
        return MissionWinStepControlInstance(**self._data[k])    
