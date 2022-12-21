
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class PrizeInstance:
    id:int # 1
    name:str # '采购币*10'
    user_exp:int # 0
    mp:int # 0
    ammo:int # 0
    mre:int # 0
    part:int # 0
    core:int # 0
    gem:int # 0
    gem_pay:int # 0
    gun_id:str # '0'
    sangvis:str # ''
    item_ids:str # '41-10'
    furniture:str # ''
    gift:str # ''
    equip_ids:str # ''
    coins:str # '1-100,2-3,3-50'
    skin:int # 0
    content:str # 'prize-20000001'
    send_limit:int # 0
    icon:str # ''
    bp_pay:int # 0
    fairy_ids:str # ''
    chip:str # ''
    commander_uniform:str # ''

class Prize(ConfigTable):
    name = 'prize'

    def add_instance(self,k):
        return PrizeInstance(**self._data[k])    
