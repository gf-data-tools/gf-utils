
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class FunctionControlInfoInstance:
    id:str # '1'
    function_name:str # 'fairy'
    turn_on:str # '1'
    need_level:str # '0'
    pre_mission:str # '0'
    need_copper_medal:str # '60'
    mall_id:str # '99007'
    max_cost_id:str # '9'
    description:str # '妖精系统'

class FunctionControlInfo(ConfigTable):
    name = 'function_control_info'

    def add_instance(self,k):
        return FunctionControlInfoInstance(**self._data[k])    
