from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ItemInstance:
    id: int  # 1
    type: int  # 1
    arg: str  # '1'
    code: str  # 'IOP_Contract'
    item_name: str  # '人形制造契约'
    introduction: str  # '委托IOP制造人形的订单。万幸，我们的老朋友一直是我们坚实的后援。'
    rank: int  # 1
    sort: int  # 10
    initial_num: str  # ''
    daily_limit: str  # ''
    upper_limit: int  # 0
    consume_type: int  # 0
    item_access: str  # '1,4,5,3'
    detail_introduction: str  # '可在工厂-人形制造中委托IOP进行人形制造。'
    is_hide_info: int  # 0


class Item(ConfigTable):
    name = "item"

    def add_instance(self, k):
        return ItemInstance(**self._data[k])
