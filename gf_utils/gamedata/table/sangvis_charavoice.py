from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SangvisCharavoiceInstance:
    id: int  # 1
    name: str  # '获得1'
    code: str  # '_GAIN01_JP'
    is_hidden: int  # 0
    is_fetter: int  # 0


class SangvisCharavoice(ConfigTable):
    name = "sangvis_charavoice"

    def add_instance(self, k):
        return SangvisCharavoiceInstance(**self._data[k])
