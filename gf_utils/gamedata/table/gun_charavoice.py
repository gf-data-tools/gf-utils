from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GunCharavoiceInstance:
    id: int  # 1
    name: str  # '获得'
    code: str  # '_GAIN_JP'
    is_hidden: int  # 0
    is_skin: int  # 0
    is_fetter: int  # 0


class GunCharavoice(ConfigTable):
    name = "gun_charavoice"

    def add_instance(self, k):
        return GunCharavoiceInstance(**self._data[k])
