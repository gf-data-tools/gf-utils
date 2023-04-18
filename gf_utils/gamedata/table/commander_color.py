from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CommanderColorInstance:
    id: int  # 1
    icon_colors: str  # '62,71,69;185,255,48'


class CommanderColor(ConfigTable):
    name = "commander_color"

    def add_instance(self, k):
        return CommanderColorInstance(**self._data[k])
