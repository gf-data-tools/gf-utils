from ._base import ConfigTable
from dataclasses import dataclass
from .battle_formula import BattleFormulaInstance
import re


@dataclass
class SkillArg:
    major:int = 1
    minor:int = 1

@dataclass
class BattleBuffInstance:    
    id: int = 83
    name: str = 'G11_二技能算子'
    description: str = ''
    conflict_type: int = 415
    max_tier: int = 30
    type: int = 500
    duration_type: int = 1
    duration: int|SkillArg = '99999'
    delay: int = 0
    probability: int = 0
    boss_available: int = 1
    armor_reduce_number: int|SkillArg = '0'
    pow_number: int|SkillArg = '0'
    dodge_number: int|SkillArg = '0'
    hit_number: int|SkillArg = '0'
    rate_number: int|SkillArg = '0'
    critical_number: int|SkillArg = '0'
    critical_damage_number: int|SkillArg = '0'
    damage_reduce_number: int|SkillArg = '0'
    damage_return_number: int|SkillArg = '0'
    move_number: int|SkillArg = '0'
    shield_number: int|SkillArg = '0'
    arp_number: int|SkillArg = '0'
    trigger_creation_id: int|SkillArg = '0'
    trigger_creation_delay: int|SkillArg = '0'
    is_form_play: int|SkillArg = 0
    buff_animation: str = ''
    buff_description: str = ''
    available_gun_type: str = ''
    available_gun_type2: str = ''
    def_number: int|SkillArg = '0'
    defbreak_number: int|SkillArg = '0'
    maxdef_number: int|SkillArg = '0'
    cdr_number: int|SkillArg = '0'
    forced_skill: int|SkillArg = '0'
    fix_damage: int|BattleFormulaInstance = 0
    night_view_percent: int|SkillArg = '0'
    range_number: int|SkillArg = '0'
    watch_id: int|BattleFormulaInstance = 0
    orb_effect: int|BattleFormulaInstance = 0
    hurt_id: int|BattleFormulaInstance = 0
    hurt_cd: int|BattleFormulaInstance = 0

class BattleBuff(ConfigTable):
    name = 'battle_buff'
    
    def __getitem__(self,k):
        modif_stats = {}
        for key, value in self._data[k].items():
            if isinstance(value, int) and value>1000000000:
                try:
                    modif_stats[key] = self.gamedata.battle_formula[value-1000000000]
                except KeyError:
                    modif_stats[key] = None
            if isinstance(value, str):
                match = re.fullmatch(r'\*([0-9])([0-9][0-9])', value)
                if match:
                    modif_stats[key] = SkillArg(major=int(match[1]),minor=int(match[2]))

        return BattleBuffInstance(**(self._data[k]|modif_stats))