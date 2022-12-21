
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class OrganizationInstance:
    id:int # 1
    parent_id:int # 0
    name:str # '格里芬'
    description:str # '总部'

class Organization(ConfigTable):
    name = 'organization'

    def add_instance(self,k):
        return OrganizationInstance(**self._data[k])    
