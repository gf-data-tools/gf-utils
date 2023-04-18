from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class GuildEmojiGroupInstance:
    id: int  # 1
    is_locked: int  # 0
    icon_emoji_code: str  # 'WeChatEmoji_happy'
    prize: str  # ''
    is_hide: int  # 0


class GuildEmojiGroup(ConfigTable):
    name = "guild_emoji_group"

    def add_instance(self, k):
        return GuildEmojiGroupInstance(**self._data[k])
