
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FurnitureInstance:
    id:int # 101
    name:str # '万圣节-哥特床'
    classes:int # 1
    type:int # 203
    position:str # '26,2'
    space:str # '6,4,1,1,2,0'
    deco_rate:int # 900
    decompose_gift:int # 100003
    description:str # '哥特床是整个万圣节体验的核心，来自黑暗时代的设计让每个入睡者都能进入瑰丽神秘的梦境，见到魔法兔子、红心女王和500秃子。'
    code:str # 'ws2016_bed'
    texture_type:str # '1'
    sorting:str # '0'
    offset:str # '0,-0.05,0'
    rotate:str # '2'
    interact_point:str # '6,104'
    interact_point_offset:str # '0.46,0.32,1|*2.65,5.203,0'
    furniture_bgm:str # '0'
    touch_area:str # '0'
    bonus_id:int # 0
    ai:int # 0

class Furniture(ConfigTable):
    name = 'furniture'

    def add_instance(self,k):
        return FurnitureInstance(**self._data[k])    
