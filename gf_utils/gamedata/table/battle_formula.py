from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class BattleFormulaInstance:
    id: int
    formula: str


class BattleFormula(ConfigTable):
    name = "battle_formula"

    def add_instance(self, k):
        return BattleFormulaInstance(**self._data[k])
