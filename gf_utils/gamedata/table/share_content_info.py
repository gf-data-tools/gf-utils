from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ShareContentInfoInstance:
    id: str  # '1'
    type: str  # '0'
    platform: str  # '23'
    title: str  # '详情'
    content: str  # 'share_content-10000001'
    description: str  # 'type0表示人形详细介面,platform23表示微信'


class ShareContentInfo(ConfigTable):
    name = "share_content_info"

    def add_instance(self, k):
        return ShareContentInfoInstance(**self._data[k])
