
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class CareerQuestGroupInstance:
    id:int # 1
    type:int # 1
    sub_type:int # 0
    title:str # '作战能力'
    sub_title:str # 'career_quest_group-20000001'
    function_control_id:int # 0

class CareerQuestGroup(ConfigTable):
    name = 'career_quest_group'

    def add_instance(self,k):
        return CareerQuestGroupInstance(**self._data[k])    
