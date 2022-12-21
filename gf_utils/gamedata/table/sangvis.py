
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SangvisInstance:
    id:int # 1001
    name:str # '稻草人'
    en_name:str # 'Scarecrow'
    code:str # 'Scarecrow'
    introduce:str # '擅长收集和分析情报，并不擅长正面作战，在铁血人形中地位较低。理性派，无口毒舌，忠于职守，鄙夷感性，面对感情丰富却只懂得服从的格里芬人形充满优越感。'
    dialogue:str # '待定，单独提出语言包最好'
    extra:str # ',,'
    en_introduce:str # '待定'
    forces:int # 1
    type:int # 1
    character:str # '2,4,6'
    formation:int # 1
    resolution:int # 101
    shape_scale:str # '80,120'
    ap_cost:int # 10
    ap_add:int # 0
    rank:int # 5
    skill1:int # 900515
    skill2_type:int # 2
    skill2:int # 30006
    skill3:int # 900511
    skill_advance:int # 900512
    skill_resolution:str # '900526,0,0,0'
    passive_skill2:str # ''
    dynamic_passive_skill:str # '900513,900514,900517'
    normal_attack:int # 900510
    baseammo:int # 10
    basemre:int # 10
    ammo_add_withnumber:int # 5
    mre_add_withnumber:int # 5
    ratio_hp:int # 95
    ratio_pow:int # 95
    ratio_rate:int # 116
    ratio_hit:int # 90
    ratio_dodge:int # 120
    ratio_armor:int # 0
    armor_piercing:int # 15
    crit:int # 20
    crit_dmg:int # 150
    eat_ratio:int # 100
    ratio_speed:int # 12
    special:int # 0
    attack_range_type:int # 2
    assist_attack_range:int # 15
    ratio_range:int # 500
    search_range:int # 7
    effect_grid_effect:str # '4:2,15;4,20'
    type_chip1:str # '1,2,3'
    type_chip2:str # '1,2,3'
    type_chip3:str # '1,2,3'
    illustration_id:int # 5
    ai:int # 11001
    is_additional:int # 1
    launch_time:str # '2016-05-20 00:00:00'
    obtain_ids:str # '0'
    display_enemy_team:int # 930001
    picture_offset:str # '-100.001,-65.021'
    picture_scale:str # '0.864,0.864'
    dorm_scale:int # 100
    org_id:int # 10604

class Sangvis(ConfigTable):
    name = 'sangvis'

    def add_instance(self,k):
        return SangvisInstance(**self._data[k])    
