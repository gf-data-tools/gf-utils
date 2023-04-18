from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MedalAppearanceInfoInstance:
    id: str  # '1'
    pic_code: str  # 'Icon_Medal_QuarterEvent'
    effect_code: str  # ''
    background_code: str  # 'Bg_IllustratedBook_MedalDetail_NEW'


class MedalAppearanceInfo(ConfigTable):
    name = "medal_appearance_info"

    def add_instance(self, k):
        return MedalAppearanceInfoInstance(**self._data[k])
