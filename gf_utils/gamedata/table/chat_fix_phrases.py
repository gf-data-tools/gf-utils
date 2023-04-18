from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class ChatFixPhrasesInstance:
    id: int  # 1
    group: int  # 2
    content: str  # '对对对!!!'
    paras: str  # ''
    type: int  # 1
    type_name: str  # '闲谈'


class ChatFixPhrases(ConfigTable):
    name = "chat_fix_phrases"

    def add_instance(self, k):
        return ChatFixPhrasesInstance(**self._data[k])
