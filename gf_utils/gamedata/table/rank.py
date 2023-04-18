from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class RankInstance:
    id: int  # 1
    name: str  # '狩猎排行'
    type: int  # 1
    sub_type: str  # '0'
    refresh: str  # 'month:1:0'
    title: str  # '每日4点刷新'
    top_rewards: str  # ''
    percentage_rewards: str  # ''
    out_rewards: str  # ''
    visable_rank: int  # 100
    score_rewards: str  # ''
    ranking_onlist_number: int  # 20000
    visable_count: int  # 100
    rank_list_num: int  # 0
    begin_show_time: str  # ''
    end_show_time: str  # ''
    prize_preview: str  # ''


class Rank(ConfigTable):
    name = "rank"

    def add_instance(self, k):
        return RankInstance(**self._data[k])
