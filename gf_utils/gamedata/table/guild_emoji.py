
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class GuildEmojiInstance:
    id:int # 1
    group:int # 1
    emoji_code:str # 'WeChatEmoji_hi'
    is_locked:int # 0
    prize:str # ''
    is_hide:int # 0

class GuildEmoji(ConfigTable):
    name = 'guild_emoji'

    def add_instance(self,k):
        return GuildEmojiInstance(**self._data[k])    
