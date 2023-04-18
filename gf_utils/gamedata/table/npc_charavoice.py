from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class NpcCharavoiceInstance:
    id: int  # 1
    name: str  # '问候'
    code: str  # '_HELLO_JP'
    kalina_favor_lv: int  # 0
    data: str  # ''
    China_data: str  # ''
    time: str  # ''


class NpcCharavoice(ConfigTable):
    name = "npc_charavoice"

    def add_instance(self, k):
        return NpcCharavoiceInstance(**self._data[k])
