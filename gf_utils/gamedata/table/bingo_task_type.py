
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class BingoTaskTypeInstance:
    id:int # 1
    task_type:str # 'mission_common_win'
    title:str # '普通战役挑战'
    content:str # '战斗胜利情况下挑战任意普通战役{0}次'
    function_control_id:int # 0

class BingoTaskType(ConfigTable):
    name = 'bingo_task_type'

    def add_instance(self,k):
        return BingoTaskTypeInstance(**self._data[k])    
