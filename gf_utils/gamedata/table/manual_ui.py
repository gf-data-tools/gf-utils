from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ManualUiInstance:
    id: int  # 10001
    code_a: str  # 'Boomer'
    description_a: str  # '我方梯队'
    description_b: str  # '歌莉娅'
    description_c: str  # '拾取'
    code_b: str  # 'Console_Icon'
    is_manual_target: int  # 0
    use_fairy_ui: int  # 0


class ManualUi(ConfigTable):
    name = "manual_ui"

    def add_instance(self, k):
        return ManualUiInstance(**self._data[k])
