from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class RankInfoInstance:
    id: str  # '1'
    name: str  # '狩猎排行'
    type: str  # '1'
    sub_type: str  # '0'
    refresh: str  # 'month:1:0'
    title: str  # '每日4点刷新'
    top_rewards: str  # ''
    percentage_rewards: str  # ''
    out_rewards: str  # ''
    visable_rank: str  # '100'
    visable_count: str  # '100'
    score_rewards: str  # ''
    ranking_onlist_number: str  # '20000'
    every_table_num: str  # '20000'
    rank_list_num: str  # '0'
    begin_refresh_time: str  # ''
    end_refresh_time: str  # ''
    begin_show_time: str  # ''
    end_show_time: str  # ''
    mission_rank_type: str  # '0'
    sub_mission_group: str  # ''
    event_rank_id: str  # '0'
    prize_preview: str  # ''


class RankInfo(ConfigTable):
    name = "rank_info"

    def add_instance(self, k):
        return RankInfoInstance(**self._data[k])
