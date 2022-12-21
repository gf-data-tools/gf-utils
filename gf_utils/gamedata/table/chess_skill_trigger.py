
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ChessSkillTriggerInstance:
    id:int # 10101
    type:str # '14'
    target:int # 3
    parameter:int # 1
    parameter2:str # '0'

class ChessSkillTrigger(ConfigTable):
    name = 'chess_skill_trigger'

    def add_instance(self,k):
        return ChessSkillTriggerInstance(**self._data[k])    
