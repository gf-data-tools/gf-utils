
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class BingoInfoInstance:
    id:str # '1'
    event_stage:str # '1'
    grid_num:str # '6'
    normal_task_num:str # '3'
    pay_task_num:str # '3'
    repeat_number_for_credit:str # '10'
    choose_number_from_credit:str # '100'
    max_pay_task_refresh_count:str # '0'
    line_prize_config:str # '30101,30102,30103,30104,30105,30106,30107,30108,30109,30110,30111,30112,30113,30114'
    final_prize_config:str # '30201_1,30202_4,30203_8,30204_14'
    cost_raffle_ticket:str # '1'
    starttime:str # '2022-10-29 00:00:00'
    endtime:str # '2022-11-18 23:59:59'
    img_1:str # 'secretkey_20221029.jpg'
    img_2:str # '0'
    img_3:str # '0'
    img_4:str # '0'
    img_5:str # '0'
    text_1:str # '宾果'
    text_2:str # '宾果'
    text_3:str # '宾果'
    text_4:str # '宾果'
    text_5:str # '宾果'

class BingoInfo(ConfigTable):
    name = 'bingo_info'

    def add_instance(self,k):
        return BingoInfoInstance(**self._data[k])    
