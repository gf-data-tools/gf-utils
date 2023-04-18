from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GiftItemInstance:
    id: int  # 1
    name: str  # '马卡洛夫-南瓜熊熊'
    type: int  # 2
    rank: int  # 6
    favor: int  # 50000
    fit_gun: int  # 8
    skin: int  # 1
    poster: int  # 30001
    code: str  # 'gift_bundle_halloween_PM'
    bonus_description: str  # '可解锁人形换装'
    description: str  # '在宿舍内赠送给对应人形，可以获得装扮、海报以及好感度奖励。'
    is_hidden: int  # 0
    exp: int  # 0
    profile_pic: int  # 0
    item_access: str  # ''
    detail_introduction: str  # 'gift_item-40000001'
    sort: int  # 0


class GiftItem(ConfigTable):
    name = "gift_item"

    def add_instance(self, k):
        return GiftItemInstance(**self._data[k])
