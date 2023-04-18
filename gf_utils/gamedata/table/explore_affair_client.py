from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ExploreAffairClientInstance:
    id: int  # 1
    area_id: str  # '1'
    weight: int  # 10
    tag_weight: str  # ''
    content: str  # '[gun1]被几个人类搭讪了，但是对方很无礼，人类与人形友好的关系史上可能又留下了一个小黑点。'
    necessary_num: str  # '1,0'
    background: str  # ''
    script_type: str  # '2'


class ExploreAffairClient(ConfigTable):
    name = "explore_affair_client"

    def add_instance(self, k):
        return ExploreAffairClientInstance(**self._data[k])
