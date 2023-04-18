from ._base import ConfigTable, SkillArg, BuffTier
from dataclasses import dataclass
import re


@dataclass
class BattleHurtConfigInstance:
    id: int  # 1
    description: str  # '普通攻击'
    damage_ratio: int | SkillArg  # '100'
    extra_damage: int | SkillArg  # '0'
    buff_id: int  # 0
    harm_delay: int | SkillArg  # '0'
    target_move: int | SkillArg  # '0'
    is_critical_hit: int  # 1
    critical_hit_rate: int | SkillArg  # '100'
    float_wide: int  # 15
    trigger_creation_id: int  # 0
    trigger_creation_delay: int  # 0
    is_form_hurt: int  # 0
    is_miss: int  # 1
    is_armor: int  # 1
    beat_back_percent: int | SkillArg  # '0'
    buff_id_target: str  # '0'
    buff_id_self: str  # '0'
    hurt_buff_trigger_type: int  # 0
    buff_rate: int | SkillArg  # '0'
    target_move_percent: int | SkillArg  # '0'
    target_skill: int  # 0
    trigger_summoner: int  # 0
    defbreak_rate: str  # '0'
    extra_defbreak: str  # '0'
    hit_type: int  # 1
    is_ricochet: int  # 0
    is_shield: int  # 0
    fix_damage: int  # 0
    ui_control: int  # 0


class BattleHurtConfig(ConfigTable):
    name = "battle_hurt_config"

    def add_instance(self, k):
        modif_stats = {}
        for key, value in self._data[k].items():
            if key == "buff_id":
                value = self.gamedata.battle_buff[self.gamedata.get_value(value)]
            elif key == "target_skill":
                value = self.gamedata.battle_skill_config[
                    self.gamedata.get_value(value)
                ]
            elif key in ["buff_id_target", "buff_id_self"]:
                if "," not in value:
                    value = [self.gamedata.get_value(value)]
                else:
                    value = self.gamedata.get_value(value)
                group = []
                for i in value:
                    if isinstance(i, list):
                        group.append(
                            BuffTier(buff=self.gamedata.battle_buff[i[0]], tier=i[1])
                        )
                    else:
                        group.append(
                            BuffTier(buff=self.gamedata.battle_buff[i], tier=0)
                        )
                value = group
            else:
                value = self.gamedata.get_value(value)

            modif_stats[key] = value
        return BattleHurtConfigInstance(**modif_stats)
