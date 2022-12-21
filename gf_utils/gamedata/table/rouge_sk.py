
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class RougeSkInstance:
    id:int # 1
    skill_id:int # 903391
    code:str # 'HS2000'
    type_c:str # '1'
    rank_c:int # 1

class RougeSk(ConfigTable):
    name = 'rouge_sk'

    def add_instance(self,k):
        return RougeSkInstance(**self._data[k])    
