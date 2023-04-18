from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MallClassificationInstance:
    id: int  # 1000
    parent_id: int  # 0
    sort: int  # 1
    name: str  # '活动'
    description: str  # '限时活动'


class MallClassification(ConfigTable):
    name = "mall_classification"

    def add_instance(self, k):
        return MallClassificationInstance(**self._data[k])
