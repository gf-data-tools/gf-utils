
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class GunInstance:
    id:int # 1
    name:str # '柯尔特左轮'
    en_name:str # 'M1873'
    code:str # 'M1873'
    introduce:str # '类型            左轮手枪\r\n总重            1,048克（7½"枪管）\r\n全长            11"（279毫米 - 5½"枪管）；\r\n                13"（318毫米 - 7½"枪管）\r\n弹药            .45柯尔特，.44-40温彻斯特，.38-40温彻斯特，.32-20温彻斯特，其他\r\n枪机种类        单动式\r\n供弹方式        6发弹巢\r\n瞄准具型式      前后准星'
    dialogue:str # '指挥官,是您在叫我嘛？您这里有可乐吗！有很多很多的可乐么！'
    extra:str # 'Saru,田中あいみ,'
    en_introduce:str # 'Type                       Revolver\n\nWeight                     1,048 g (with 7½" barrel)\n\nLength                     11" (279 mm – with 5½" barrel);\n\n                           12.5" (318 mm – with 7½" barrel)\n\nCartridge                  .45 Colt, .44-40 WCF, .38-40 WCF,\n\n                           .32-20 WCF, .38 Colt and many others,\n\n                           including .22 LR, .38 Special,\n\n                           .357 Magnum and .44 Special\n\nAction                     Single-action revolver\n\nFeed system                6-shot Cylinder'
    character:str # 'gun-60000001'
    type:int # 1
    rank:int # 4
    develop_duration:int # 3000
    baseammo:int # 10
    basemre:int # 10
    ammo_add_withnumber:int # 5
    mre_add_withnumber:int # 5
    retiremp:int # 2
    retireammo:int # 2
    retiremre:int # 2
    retirepart:int # 0
    ratio_life:int # 120
    ratio_pow:int # 125
    ratio_rate:int # 85
    ratio_speed:int # 100
    ratio_hit:int # 90
    ratio_dodge:int # 95
    ratio_armor:int # 0
    armor_piercing:int # 15
    crit:int # 20
    special:int # 0
    eat_ratio:int # 130
    ratio_range:int # 95
    skill1:int # 100503
    skill2:int # 0
    normal_attack:int # 300115
    passive_skill:str # ''
    dynamic_passive_skill:str # ''
    effect_grid_center:int # 13
    effect_guntype:str # '0'
    effect_grid_pos:str # '8,12,14,18'
    effect_grid_effect:str # '1,12;3,25'
    max_equip:int # 0
    type_equip1:str # '1;4,13,16,18'
    type_equip2:str # '2;6'
    type_equip3:str # '3;10'
    type_equip4:str # ''
    ai:int # 1
    is_additional:int # 0
    launch_time:str # '2016-05-20 00:00:00'
    obtain_ids:str # '1,3'
    rank_display:int # 4
    prize_id:int # 0
    mindupdate_consume:str # '10:20,45:200;10:40,45:1000;10:60,45:2000'
    explore_tag:str # '52'
    gun_detail_bg:str # 'nation_US'
    org_id:int # 10302
    related_story_id:int # 100001
    show_damage_skin:str # ',2105,'

class Gun(ConfigTable):
    name = 'gun'

    def add_instance(self,k):
        return GunInstance(**self._data[k])    
