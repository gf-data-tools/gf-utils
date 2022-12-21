
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class CarnivalInfoInstance:
    id:str # '8'
    name:str # '露落苍穹'
    pt_item_id:str # '110052'
    pt_gift:str # '100:10100,200:10101,500:10102,800:10103,1200:10104,1800:10105,2000:10106,2400:10107,3000:10108'
    start_time:str # '2022-08-04 00:00:00'
    banner:str # 'carnival_220804.jpg'
    end_time:str # '2022-08-24 23:59:59'
    label_ids:str # '20,21,22'

class CarnivalInfo(ConfigTable):
    name = 'carnival_info'

    def add_instance(self,k):
        return CarnivalInfoInstance(**self._data[k])    
