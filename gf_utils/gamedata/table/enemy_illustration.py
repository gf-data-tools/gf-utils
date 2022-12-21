
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class EnemyIllustrationInstance:
    id:int # 1
    name:str # '工蜂型民用靶机'
    type:int # 2
    code:str # 'Drone'
    introduce:str # '常规靶机，只用于训练和演习，可自动记录作战影像（前提是摄像头没被破坏）。'
    forces:int # 0
    if_capture:int # 0
    pow_rank:int # 0
    life_rank:int # 7
    hit_rank:int # 0
    dodge_rank:int # 0
    rate_rank:int # 0
    armor_rank:int # 0
    speed_rank:int # 0
    range_rank:int # 0
    counter:str # '努力训练!'
    character:str # '1001,903'
    enemy_skill:str # ''
    launch_time:str # '2016-5-20 00:00:00'
    extra:str # 'enemy_illustration-40000001'
    spine_scale:str # '90,90,1'
    org_id:int # 0
    related_story_id:int # 0

class EnemyIllustration(ConfigTable):
    name = 'enemy_illustration'

    def add_instance(self,k):
        return EnemyIllustrationInstance(**self._data[k])    
