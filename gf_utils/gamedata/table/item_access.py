
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ItemAccessInstance:
    id:int # 1
    name:str # '商城'
    carnival_goto_page_id:int # -1
    function_control_id:int # 0

class ItemAccess(ConfigTable):
    name = 'item_access'

    def add_instance(self,k):
        return ItemAccessInstance(**self._data[k])    
