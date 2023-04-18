from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TutorialManualInstance:
    id: int  # 100
    type: int  # 1
    child_ids: str  # '101,102,103,104,105,106,107,108,109'
    title: str  # '基地导览'
    sub_title: str  # '指挥官，请先熟悉一下基地吧~'
    code: str  # 'manual_base'
    content: str  # ''
    function_control_id: int  # 0
    goto_page: int  # 0


class TutorialManual(ConfigTable):
    name = "tutorial_manual"

    def add_instance(self, k):
        return TutorialManualInstance(**self._data[k])
