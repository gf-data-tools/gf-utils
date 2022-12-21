
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class GunExpInfoInstance:
    lv:str # '1'
    exp:str # '100'

class GunExpInfo(ConfigTable):
    name = 'gun_exp_info'

    def add_instance(self,k):
        return GunExpInfoInstance(**self._data[k])    
