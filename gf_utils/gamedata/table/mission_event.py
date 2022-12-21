
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class MissionEventInstance:
    id:int # 1
    type:int # 2
    mission_campaign:str # '-2,-3,-4'
    draw_event_id:str # ''
    start_time:str # ''
    end_time:str # ''
    init_mission_id:str # '10005'
    function_control_id:str # ''
    open_mission:str # ''
    open_time:str # ''
    mission_event_opentime_white_list:str # ''

class MissionEvent(ConfigTable):
    name = 'mission_event'

    def add_instance(self,k):
        return MissionEventInstance(**self._data[k])    
