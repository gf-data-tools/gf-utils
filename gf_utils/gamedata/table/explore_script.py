from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ExploreScriptInstance:
    id: int  # 1
    type: int  # 5
    code: str  # 'sample501'


class ExploreScript(ConfigTable):
    name = "explore_script"

    def add_instance(self, k):
        return ExploreScriptInstance(**self._data[k])
