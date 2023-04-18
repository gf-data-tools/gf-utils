from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ExploreAffairServerInstance:
    id: int  # 1
    content: str  # '[pet1]来到[gun1]的身边，但被枪吓到逃跑了，只留下了一件装备。'
    background: str  # ''
    script_type: str  # '2'


class ExploreAffairServer(ConfigTable):
    name = "explore_affair_server"

    def add_instance(self, k):
        return ExploreAffairServerInstance(**self._data[k])
