from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CarnivalGotoPageInfoInstance:
    id: str  # '1'
    type: str  # 'buy_bp_count'
    goto_page: str  # 'Mall-5'


class CarnivalGotoPageInfo(ConfigTable):
    name = "carnival_goto_page_info"

    def add_instance(self, k):
        return CarnivalGotoPageInfoInstance(**self._data[k])
