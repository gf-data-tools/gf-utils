from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class GuildFlagInstance:
    id: int  # 1
    type: int  # 1
    pattern_code: str  # ''
    texture: str  # ''
    color: str  # ''


class GuildFlag(ConfigTable):
    name = "guild_flag"

    def add_instance(self, k):
        return GuildFlagInstance(**self._data[k])
