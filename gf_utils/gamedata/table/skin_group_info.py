from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class SkinGroupInfoInstance:
    id: str  # '1'
    theme: str  # '狩猎圣诞老人行动'
    skin: str  # '301,302,303,304,305,306,307,308,309,310'
    description: str  # '格里芬即将迎来第一个圣诞夜，正在大家在晚宴和余兴节目之间忙碌时，一个疯狂的计划正在几个危险人形中酝酿……'
    bonus: str  # '0'
    note: str  # '0'
    icon: str  # 'sd2016_tree_icon'
    order: str  # '4'
    is_new: str  # '0'
    title_code: str  # 'sd2016'


class SkinGroupInfo(ConfigTable):
    name = "skin_group_info"

    def add_instance(self, k):
        return SkinGroupInfoInstance(**self._data[k])
