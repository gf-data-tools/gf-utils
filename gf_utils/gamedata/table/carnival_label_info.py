
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class CarnivalLabelInfoInstance:
    id:str # '20'
    start_time:str # '2022-08-04 00:00:00'
    label_text:str # '第一阶'
    carnival_tasks:str # '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27'

class CarnivalLabelInfo(ConfigTable):
    name = 'carnival_label_info'

    def add_instance(self,k):
        return CarnivalLabelInfoInstance(**self._data[k])    
