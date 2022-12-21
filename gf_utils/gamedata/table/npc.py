
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class NpcInstance:
    id:int # -14
    name:str # '格里芬'
    code:str # 'Org_Griffin'
    title:str # '格里芬'
    ai:int # 9999
    is_adjutant:int # 0
    unlock_text:str # 'npc-29999986'
    mission_id:int # 0
    item_id:int # 0
    skin_code:str # ''
    voice_code:str # ''
    org_id:str # '101'
    org_introduction:str # '狮鹫每接近天空一尺，就需要部门间的配合更默契一分。'

class Npc(ConfigTable):
    name = 'npc'

    def add_instance(self,k):
        return NpcInstance(**self._data[k])    
