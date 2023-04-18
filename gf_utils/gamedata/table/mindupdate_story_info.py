from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class MindupdateStoryInfoInstance:
    id: str  # '1'
    gun_id: str  # '2'
    stage_id: str  # '1'
    description: str  # ''
    scripts: str  # '2_1'
    title: str  # ''
    prize_id: str  # '4001'


class MindupdateStoryInfo(ConfigTable):
    name = "mindupdate_story_info"

    def add_instance(self, k):
        return MindupdateStoryInfoInstance(**self._data[k])
