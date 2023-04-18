from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class OperationInfoInstance:
    id: str  # '1'
    campaign: str  # '0'
    name: str  # '应援训练'
    description: str  # '战斗梯队正在休整,支援梯队将负责维持该地区秩序。'
    duration: str  # '3000'
    mp: str  # '0'
    ammo: str  # '145'
    mre: str  # '145'
    part: str  # '0'
    item_pool: str  # '3,4,0'
    team_leader_min_level: str  # '40'
    gun_min: str  # '4'
    guntype1_min: str  # '0'
    guntype2_min: str  # '0'
    guntype3_min: str  # '1'
    guntype4_min: str  # '0'
    guntype5_min: str  # '0'
    guntype6_min: str  # '0'
    guntype7_min: str  # '0'


class OperationInfo(ConfigTable):
    name = "operation_info"

    def add_instance(self, k):
        return OperationInfoInstance(**self._data[k])
