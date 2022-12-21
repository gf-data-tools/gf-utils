
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionWinTypeConfigInstance:
    id:int # 1
    type:int # 1102
    arguments:str # '1'
    extra_language:str # 'mission_win_type_config-10000001'
    is_hidden:int # 0
    is_show_count:str # '1'

class MissionWinTypeConfig(ConfigTable):
    name = 'mission_win_type_config'

    def add_instance(self,k):
        return MissionWinTypeConfigInstance(**self._data[k])    
