from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class DormEmojiTextInfoInstance:
    id: str  # '102101'
    text: str  # '♪Сакварлис саплавс ведзебди'


class DormEmojiTextInfo(ConfigTable):
    name = "dorm_emoji_text_info"

    def add_instance(self, k):
        return DormEmojiTextInfoInstance(**self._data[k])
