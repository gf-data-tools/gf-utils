
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FairyTalentTypeInstance:
    id:int # 1
    name:str # '特殊型'

class FairyTalentType(ConfigTable):
    name = 'fairy_talent_type'

    def add_instance(self,k):
        return FairyTalentTypeInstance(**self._data[k])    
