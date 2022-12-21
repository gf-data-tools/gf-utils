
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class CarnivalTaskTypeInstance:
    id:int # 1
    type:str # 'cumulative_login'
    title:str # '累计登录'
    content:str # '累计登录{0}天'
    function_control_id:int # 0

class CarnivalTaskType(ConfigTable):
    name = 'carnival_task_type'

    def add_instance(self,k):
        return CarnivalTaskTypeInstance(**self._data[k])    
