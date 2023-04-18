from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FairyCharavoiceInstance:
    id: int  # 1
    name: str  # '交流1'
    code: str  # '_DIALOGUE1_JP'
    is_hidden: int  # 0
    is_fetter: int  # 0


class FairyCharavoice(ConfigTable):
    name = "fairy_charavoice"

    def add_instance(self, k):
        return FairyCharavoiceInstance(**self._data[k])
