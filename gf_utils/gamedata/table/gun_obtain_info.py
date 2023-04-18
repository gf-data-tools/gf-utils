from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GunObtainInfoInstance:
    obtain_id: str  # '0'
    description: str  # '暂时无法获取,请期待后续活动'
    detail: str  # '0'
    goto_page_id: str  # '0'


class GunObtainInfo(ConfigTable):
    name = "gun_obtain_info"

    def add_instance(self, k):
        return GunObtainInfoInstance(**self._data[k])
