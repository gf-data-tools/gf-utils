from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GunTagInfoInstance:
    id: str  # '101'
    tag: str  # '前排'
    tag_type: str  # '1'
    description: str  # '该人形生存能力较强，编成时适合放置在队伍前排。'


class GunTagInfo(ConfigTable):
    name = "gun_tag_info"

    def add_instance(self, k):
        return GunTagInfoInstance(**self._data[k])
