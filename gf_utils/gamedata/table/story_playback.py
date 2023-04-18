from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class StoryPlaybackInstance:
    id: int  # 1
    story_campaign_id: str  # '0'
    name: str  # '第零战役'
    chapter: str  # '0'
    type: int  # 1
    game_chronicle: str  # ''
    description: str  # 'story_playback-30000001'
    is_hide: int  # 0


class StoryPlayback(ConfigTable):
    name = "story_playback"

    def add_instance(self, k):
        return StoryPlaybackInstance(**self._data[k])
