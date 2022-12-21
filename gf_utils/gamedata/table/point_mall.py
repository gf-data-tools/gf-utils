
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class PointMallInstance:
    id:int # 101
    type:int # 4
    gem_pay:int # 60
    gem:int # 60
    double_gem_pay:int # 60
    double_gem:int # 120
    mp:int # 0
    ammo:int # 0
    mre:int # 0
    part:int # 0
    icon:str # ''
    month_card_type:str # ''
    quota_num:int # 0
    prize_id:int # 0
    classification_id:int # 2000
    description:str # ''
    clear_type:int # 0
    clear_parameter:str # '0'

class PointMall(ConfigTable):
    name = 'point_mall'

    def add_instance(self,k):
        return PointMallInstance(**self._data[k])    
