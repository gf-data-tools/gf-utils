
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class DrawEventInfoInstance:
    id:str # '1'
    item_id:str # '100001'
    start_time:str # '2016-12-10 00:00:00'
    end_time:str # '2016-12-20 00:00:00'
    drop_ids:str # '149:1,150:2,299:1,300:3,449:1,450:4,599:1,600:5,749:1,750:6,899:1,900:7,998:1,999:10,1049:1,1050:8,1199:1,1200:9,3000:1'
    title_res:str # 'draw_title_170120.png'
    amount_coordinate:str # '370,228'
    bg_res:str # 'draw_content_170120.jpg'
    is_mail:str # '1'
    mail_type:str # '1'
    is_show:str # '1'
    clear_cycle:str # '0'
    clear_time:str # '0'
    prize_skip:str # ''
    mission_show_prize:str # '0'
    use_animation:str # '0'
    goto_to_mall:str # '0'
    can_ten_draws:str # '0'
    can_get_rewards:str # '0'
    goto_page:str # '0'
    type:str # '1'
    mission_prize_type:str # '0'
    extra_bonus:str # ''
    bonus_percent:str # '0'

class DrawEventInfo(ConfigTable):
    name = 'draw_event_info'

    def add_instance(self,k):
        return DrawEventInfoInstance(**self._data[k])    
