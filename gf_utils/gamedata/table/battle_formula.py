from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleFormulaInstance:
    id: int
    formula: str


class BattleFormula(ConfigTable):
    name = "battle_formula"

    def add_instance(self, k):
        return BattleFormulaInstance(**self._data[k])
