from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChatChannelInstance:
    id: int  # 1
    name: str  # '系统'
    if_input: int  # 0
    is_fixed_phrases: int  # 0


class ChatChannel(ConfigTable):
    name = "chat_channel"

    def add_instance(self, k):
        return ChatChannelInstance(**self._data[k])
