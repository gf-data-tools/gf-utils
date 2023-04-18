from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EventRankInstance:
    id: int  # 1
    title: str  # '19年夏活秃洞'
    remake_id: int  # 0
    weight: float  # 1.0


class EventRank(ConfigTable):
    name = "event_rank"

    def add_instance(self, k):
        return EventRankInstance(**self._data[k])
