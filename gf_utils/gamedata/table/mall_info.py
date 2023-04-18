from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MallInfoInstance:
    id: str  # '1'
    type: str  # '2'
    sort: str  # '0'
    item_ids: str  # '0'
    gem: str  # '0'
    mp: str  # '1500'
    ammo: str  # '0'
    mre: str  # '0'
    part: str  # '0'
    bp_pay: str  # '0'
    skin: str  # '0'
    gift: str  # ''
    gemprice: str  # '180'
    original_price: str  # '0'
    pointprice: str  # '0'
    if_cheap: str  # '0'
    quota: str  # '0'
    giftbag_name: str  # 'mall-10000001'
    event_code: str  # '0'
    icon: str  # ''
    daily_quota: str  # '0'
    tips: str  # ''
    discount: str  # '1.00'
    sale_starttime: str  # '0'
    sale_endtime: str  # '0'
    label: str  # '0'
    prize_id: str  # '0'
    pay_type: str  # '0'
    itemprice: str  # '0'
    on_sale_days: str  # '0'
    price_up: str  # '0'
    classification_id: str  # '5001'
    description: str  # ''
    special_daily_quota: str  # '0'


class MallInfo(ConfigTable):
    name = "mall_info"

    def add_instance(self, k):
        return MallInfoInstance(**self._data[k])
