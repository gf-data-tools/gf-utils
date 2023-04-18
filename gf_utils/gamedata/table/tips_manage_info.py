from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class TipsManageInfoInstance:
    id: str  # '1'
    title: str  # 'test'
    regTarget: str  # 'Formation://Canvas'
    targetPath: str  # 'Formation://Canvas/Top/TopBackground'
    tipsManagePath: str  # 'TipsSystem'
    tipManagePos: str  # '443,35,-251'
    tipManageSize: str  # '152,76'


class TipsManageInfo(ConfigTable):
    name = "tips_manage_info"

    def add_instance(self, k):
        return TipsManageInfoInstance(**self._data[k])
