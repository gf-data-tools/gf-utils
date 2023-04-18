from ..stc_data import GameData as _GameData
from .table import *
from .table.battle_formula import BattleFormulaInstance
from .table._base import SkillArg
import re


class GameData(_GameData):
    def get_value(self, value: str | int) -> int | SkillArg | BattleFormulaInstance:
        if isinstance(value, str):
            if not value:
                return 0
            elif match := re.fullmatch(r"\*([0-9]{4,10})", value):
                return self.get_value(100000000 + int(match[1]))
            elif match := re.fullmatch(r"\*([0-9])([0-9][0-9])", value):
                return SkillArg(major=int(match[1]), minor=int(match[2]))
            elif match := re.fullmatch(r"[0-9]+\.[0-9][0-9]+", value):
                return float(value)
            elif match := re.fullmatch(r"[0-9]+", value):
                return self.get_value(int(value))
            elif "," in value:
                return [self.get_value(i) for i in value.split(",")]
            elif ":" in value:
                return [self.get_value(i) for i in value.split(":")]
            else:
                return value
        elif isinstance(value, int):
            if value > 100000000:
                print(self.battle_formula[value % 100000000])
                try:
                    return self.battle_formula[value % 100000000]
                except KeyError:
                    return value
            else:
                return value

    def __init__(self, stc_dir, table_dir=None, to_dict=True) -> None:
        super().__init__(stc_dir, table_dir, to_dict)
        self.battle_action_config = BattleActionConfig(self)
        self.battle_buff = BattleBuff(self)
        self.battle_creation = BattleCreation(self)
        self.battle_formula = BattleFormula(self)
        self.battle_hurt_config = BattleHurtConfig(self)
        self.battle_movement_info = BattleMovementInfo(self)
        self.battle_skill_config = BattleSkillConfig(self)
        self.battle_skill_type_config = BattleSkillTypeConfig(self)
        self.battle_target_select_ai = BattleTargetSelectAi(self)
        self.battle_trigger = BattleTrigger(self)
        self.battle_watch = BattleWatch(self)
        self.battle_watch_trigger = BattleWatchTrigger(self)
