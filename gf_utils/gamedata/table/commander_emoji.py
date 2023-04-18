from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class CommanderEmojiInstance:
    id: int  # 1
    content: str  # 'Emoji_cmd_1'
    is_show: int  # 1
    required_level: int  # 0
    required_comfort: int  # 0


class CommanderEmoji(ConfigTable):
    name = "commander_emoji"

    def add_instance(self, k):
        return CommanderEmojiInstance(**self._data[k])
