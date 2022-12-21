
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ChessChipInstance:
    id:int # 10101
    code:str # 'ChipIcons_01'
    chip_up_exp:int # 1
    chip_group:int # 101
    level:int # 1
    name:str # '轻量化'
    description:str # '使用道具时，本回合手枪行动力+1。'
    cd_type:int # 0
    init_cd:int # 0
    cd:int # 0
    rank:int # 1
    number:int # 8
    skill_target_first:str # '10101'
    skill_target_second:str # '0'
    use_stage:str # '0'
    target_select_first:int # 5
    target_select_second:int # 0
    type:int # 1
    is_active:int # 0
    price:str # '2'
    sell_price:int # 2
    experience:int # 1
    init_time:int # 1
    fit_gun_type:str # '1'
    custom_type:str # ''
    show_ui:int # 0
    log_description:str # 'chess_chip-30010101'
    ai_skill:str # ''
    cutin_animation_duration:float # 0.0

class ChessChip(ConfigTable):
    name = 'chess_chip'

    def add_instance(self,k):
        return ChessChipInstance(**self._data[k])    
