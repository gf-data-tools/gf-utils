
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FetterSkillInstance:
    id:int # 1
    name:str # '极速狂花'
    code:str # 'PzB39andGrizzly'
    description:str # '火力号令对自身和PzB39效果额外增加10%。'
    gun_group:str # '96,180'
    gun:int # 96
    type:int # 1
    skill1:int # 190101
    skill2:int # 0
    normal_attack:int # 0
    passive_skill:str # ''
    dynamic_passive_skill:str # ''
    active_trigger:str # '0'

class FetterSkill(ConfigTable):
    name = 'fetter_skill'

    def add_instance(self,k):
        return FetterSkillInstance(**self._data[k])    
