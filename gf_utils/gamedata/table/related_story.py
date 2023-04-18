from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class RelatedStoryInstance:
    id: int  # 100001
    story_campaign_id: str  # '11'
    mindupdate_story_id: int  # 1
    fetter_id: str  # ''
    skin_id: str  # '301,2105'


class RelatedStory(ConfigTable):
    name = "related_story"

    def add_instance(self, k):
        return RelatedStoryInstance(**self._data[k])
