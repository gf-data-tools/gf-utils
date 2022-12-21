
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FairyLive2dInfoInstance:
    id:str # '1'
    motions:str # '101,102,103,104,105,106'
    code:str # 'fortress'
    fit_fairy:str # '14'
    skin:str # '40'

class FairyLive2dInfo(ConfigTable):
    name = 'fairy_live2d_info'

    def add_instance(self,k):
        return FairyLive2dInfoInstance(**self._data[k])    
