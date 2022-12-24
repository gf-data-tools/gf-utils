
from ._base import ConfigTable, BuffTier
from dataclasses import dataclass

@dataclass
class BattleCreationInstance:
    id:int # 1
    name:str # '手枪子弹'
    code:str # 'bullet/bullet2'
    start_type:str # '1'
    start_offset:str # '0'
    destination_type:str # '5'
    destination_offset:str # '0'
    decision_offset:str # '0'
    is_form_offset:int # 1
    is_form_offset_start:int # 1
    is_tracing:int # 0
    is_clone:int # 0
    random_number:str # '0'
    random_offset:str # '0'
    route_type:int # 1
    route_hight:int # 0
    speed:int # 5000
    easing_type:int # 0
    spin_velocity:int # 0
    rotate:str # '0'
    exist_duration:str # '0'
    effect_type:int # 0
    effect_area:int # 1
    effect_param_1:str # '0'
    effect_param_2:str # '0'
    hurt_id:str # '1'
    hurt_cd:str # '0'
    buff_id:str # '0'
    buff_type:str # '0'
    buff_cd:str # '0'
    is_single_hurt:int # 0
    is_form_play:int # 1
    creation_type:int # 0
    scale:str # '0.35,0.35,1'
    trigger_creation_id:str # ''
    trigger_creation_delay:str # ''
    sound_order:str # 'BT_pistol'
    sound_delay:str # '0'
    summoner_order:str # ''
    summoner_delay:str # ''
    is_die_delete:int # 0
    edge_indicator:str # '0'
    still_exist:int # 0
    is_orb_effect:int # 1
    is_stay_trigger:int # 0
    active_times:int # 0

class BattleCreation(ConfigTable):
    name = 'battle_creation'

    def add_instance(self,k):
        modif_stats = {}
        for key, value in self._data[k].items():
            if key=='trigger_creation_id':
                value = self.gamedata.battle_creation[self.gamedata.get_value(value)]
            if key=='hurt_id':
                value = self.gamedata.battle_hurt_config[self.gamedata.get_value(value)]
            elif key=='buff_id':
                if ',' not in value:
                    value = [self.gamedata.get_value(value)]
                else:
                    value = self.gamedata.get_value(value)
                group = []
                for i in value:
                    if isinstance(i,list):
                        group.append(BuffTier(buff=self.gamedata.battle_buff[i[0]],tier=i[1]))
                    else:
                        group.append(BuffTier(buff=self.gamedata.battle_buff[i],tier=0))
                value = group
            else:
                value = self.gamedata.get_value(value)

            modif_stats[key]=value
        return BattleCreationInstance(**modif_stats)    
