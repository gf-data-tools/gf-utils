
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class TheaterInstance:
    id:int # 41
    name:str # '灰烬山丘'
    type:int # 1
    gauge:int # 195000000
    area:str # '411,412,413,414,415,416,417,418'
    formation_limit:int # 3
    ssoc_limit:int # 5
    hoc_formation_number:int # 3
    hoc_limit:int # 3
    theater_event_id:int # 4
    rank:int # 1
    tips:str # ''
    code:str # 'Theater1'
    reinforce_coef:int # 500
    background_mask:str # '1,0,0,0,123,155,255,255,127,128,133,108,0,0.025,0.008,0.45,0.07,0.98'
    bgm:str # 'GF_Warzone_Phase1'
    advantage_bonus:int # 0
    mask_offset:str # '-500,300'
    boss_bgm:str # ''
    occupied_prize:int # 10101
    occupied_prize_display:str # '9:20,4:5'

class Theater(ConfigTable):
    name = 'theater'

    def add_instance(self,k):
        return TheaterInstance(**self._data[k])    
