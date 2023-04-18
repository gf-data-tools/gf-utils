from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MallInstance:
    id: int  # 1
    type: int  # 2
    sort: int  # 0
    item_ids: str  # '0'
    gem: int  # 0
    mp: int  # 1500
    ammo: int  # 0
    mre: int  # 0
    part: int  # 0
    bp_pay: int  # 0
    skin: int  # 0
    gift: str  # ''
    gemprice: int  # 180
    original_price: int  # 0
    pointprice: int  # 0
    if_cheap: int  # 0
    quota: int  # 0
    giftbag_name: str  # 'mall-10000001'
    event_code: str  # '0'
    icon: str  # ''
    daily_quota: int  # 0
    tips: str  # ''
    discount: float  # 1.0
    sale_starttime: int  # 0
    sale_endtime: int  # 0
    label: int  # 0
    prize_id: int  # 0
    pay_type: int  # 0
    itemprice: str  # '0'
    on_sale_days: int  # 0
    price_up: int  # 0
    classification_id: int  # 5001
    description: str  # ''


class Mall(ConfigTable):
    name = "mall"

    def add_instance(self, k):
        return MallInstance(**self._data[k])
