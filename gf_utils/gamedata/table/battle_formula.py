from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class BattleFormulaInstance:
    id: int
    formula: str

class BattleFormula(ConfigTable):
    name = 'battle_formula'

    def __getitem__(self,k):
        return BattleFormulaInstance(**self._data[k])