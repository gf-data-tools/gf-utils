from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class DrawEventInstance:
    id: int  # 1
    item_id: int  # 100001
    type: int  # 1
    start_time: str  # '2016-12-10 00:00:00'
    end_time: str  # '2016-12-20 00:00:00'
    drop_ids: str  # '149:1,150:2,299:1,300:3,449:1,450:4,599:1,600:5,749:1,750:6,899:1,900:7,998:1,999:10,1049:1,1050:8,1199:1,1200:9,3000:1'
    title_res: str  # 'draw_title_170120.png'
    amount_coordinate: str  # '370,228'
    bg_res: str  # 'draw_content_170120.jpg'
    is_mail: int  # 1
    mail_type: int  # 1
    is_show: int  # 1
    clear_cycle: int  # 0
    clear_time: str  # '0'
    prize_skip: str  # ''
    mission_show_prize: int  # 0
    use_animation: int  # 0
    goto_to_mall: int  # 0
    can_ten_draws: int  # 0
    can_get_rewards: int  # 0
    goto_page: int  # 0
    extra_bonus: str  # ''
    bonus_percent: int  # 0


class DrawEvent(ConfigTable):
    name = "draw_event"

    def add_instance(self, k):
        return DrawEventInstance(**self._data[k])
