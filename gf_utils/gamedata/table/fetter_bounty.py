from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FetterBountyInstance:
    id: int  # 101
    fetter_id: int  # 1
    type: str  # 'collect'
    value: str  # 'g:9'
    point: int  # 10
    name: str  # '人形收集'
    description: str  # '收集{0}。'


class FetterBounty(ConfigTable):
    name = "fetter_bounty"

    def add_instance(self, k):
        return FetterBountyInstance(**self._data[k])
