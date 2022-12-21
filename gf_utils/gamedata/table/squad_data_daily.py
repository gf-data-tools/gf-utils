
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadDataDailyInstance:
    id:int # 1
    title:str # '情报任务I'
    content:str # '战役胜利情况下完成任意战役1次(自律作战除外)'
    type:str # 'mission:optional'
    count:int # 1
    rank:int # 1
    prize:str # '10,3'

class SquadDataDaily(ConfigTable):
    name = 'squad_data_daily'

    def add_instance(self,k):
        return SquadDataDailyInstance(**self._data[k])    
