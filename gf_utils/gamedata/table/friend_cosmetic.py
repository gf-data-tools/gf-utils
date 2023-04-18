from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FriendCosmeticInstance:
    id: int  # 1
    item_id: int  # 1001
    sub_type: int  # 1
    mp: int  # 0
    ammo: int  # 0
    mre: int  # 0
    part: int  # 0
    gem: int  # 40
    item_ids: str  # '508-1000'
    onsale: int  # 1
    in_gasha: int  # 100
    code: str  # 'profilePic_rank2_AAT-52.png'
    order: int  # 1
    rarity: int  # 2
    decompose_gift: str  # '100001:1'
    skin: int  # 0
    is_live2d: int  # 0
    filter_type: str  # '5'
    frame_id: int  # 0
    logo_code: str  # ''


class FriendCosmetic(ConfigTable):
    name = "friend_cosmetic"

    def add_instance(self, k):
        return FriendCosmeticInstance(**self._data[k])
