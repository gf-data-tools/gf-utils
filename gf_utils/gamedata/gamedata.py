from ..stc_data import GameData as _GameData
from .table import *

class GameData(_GameData):
    def __init__(self, stc_dir, table_dir=None, to_dict=True) -> None:
        super().__init__(stc_dir, table_dir, to_dict)
        self.achievement = Achievement(self)
        self.battle_buff = BattleBuff(self)
        self.battle_formula = BattleFormula(self)