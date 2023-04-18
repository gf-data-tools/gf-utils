from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class SkinBonusInfoInstance:
    id: str  # '101'
    name: str  # '圣诞雪妖精'
    description: str  # '来自圣诞节索米小姐的一刻，但没人能明确说出发生了什么——“肯定是裙子被掀了，”AK47说，“虽然当着大家的面不知道有什么可害羞的，也就多个指挥官罢了。”“这就是演技的所在了”，马卡洛夫冷笑着评论道。'
    skin_theme: str  # '1'
    active_num: str  # '3'
    prize: str  # '9101'
    type: str  # '外观·头像'
    icon: str  # '2016xmas_01'


class SkinBonusInfo(ConfigTable):
    name = "skin_bonus_info"

    def add_instance(self, k):
        return SkinBonusInfoInstance(**self._data[k])
