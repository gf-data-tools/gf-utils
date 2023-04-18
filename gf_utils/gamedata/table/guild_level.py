from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class GuildLevelInstance:
    lv: int  # 1
    exp: int  # 0
    max_member_num: int  # 10
    max_vice_num: int  # 1
    unlock_empty_room_id: str  # ''
    unlock_room_type_id: str  # ''
    title: str  # 'guild_level-10000001'
    title_medal_code: str  # ''


class GuildLevel(ConfigTable):
    name = "guild_level"

    def add_instance(self, k):
        return GuildLevelInstance(**self._data[k])
