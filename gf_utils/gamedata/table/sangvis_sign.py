
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SangvisSignInstance:
    id:int # 1
    name:str # 'sangvis_logo1'

class SangvisSign(ConfigTable):
    name = 'sangvis_sign'

    def add_instance(self,k):
        return SangvisSignInstance(**self._data[k])    
