
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadCpuInstance:
    id:int # 1001
    color:int # 2
    grid1:int # 101
    grid2:int # 102
    grid3:int # 103
    grid4:int # 104
    grid5:int # 105
    cpu_bonus:int # 101

class SquadCpu(ConfigTable):
    name = 'squad_cpu'

    def add_instance(self,k):
        return SquadCpuInstance(**self._data[k])    
