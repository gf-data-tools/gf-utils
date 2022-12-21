
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionTargettrainBattlesettingInstance:
    difficult_level:int # 1
    dodge_level:str # '0,4,11,24,60'
    dodge_default_level:int # 1
    guard_level:str # '0,18,36,72,120'
    guard_default_level:int # 1
    shield_level:str # '0,2500,5000,7500,10000'
    shield_default_level:int # 1
    forcefield_level:str # '0,640,1600,3200,5400'
    forcefield_default_level:int # 1

class MissionTargettrainBattlesetting(ConfigTable):
    name = 'mission_targettrain_battlesetting'

    def add_instance(self,k):
        return MissionTargettrainBattlesettingInstance(**self._data[k])    
