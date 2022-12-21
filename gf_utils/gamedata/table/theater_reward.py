
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class TheaterRewardInstance:
    id:int # 101
    type:int # 1
    prize_id:str # '305:40,48:500,9:100,46:500,506:500'
    rank:str # 'No.1'
    theater_event_id:int # 4

class TheaterReward(ConfigTable):
    name = 'theater_reward'

    def add_instance(self,k):
        return TheaterRewardInstance(**self._data[k])    
