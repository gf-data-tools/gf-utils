
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FairySkinInfoInstance:
    id:str # '1'
    name:str # '勇士妖精'
    skin_name:str # '1阶默认皮肤'
    pic_id:str # 'fighting_1'
    gift_fairy:str # '1'
    ai:str # '1000'
    is_hidden:str # '0'
    strengthen_lv:str # '1'

class FairySkinInfo(ConfigTable):
    name = 'fairy_skin_info'

    def add_instance(self,k):
        return FairySkinInfoInstance(**self._data[k])    
