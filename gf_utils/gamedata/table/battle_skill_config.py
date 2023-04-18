from ._base import ConfigTable, BuffTier
from dataclasses import dataclass


@dataclass
class SkinAction:
    skin: int
    action: int


@dataclass
class BattleSkillConfigInstance:
    id: int  # 10010101
    name: str  # '火力专注'
    skill_group_id: int  # 100101
    level: int  # 1
    type: int  # 1
    skill_priority: int  # 2
    cd_type: int  # 1
    cd_time: int  # 300
    start_cd_time: int  # 150
    trigger_id: str  # '0'
    trigger_type: int  # 1
    trigger_target: int  # 1
    trigger_parameter: str  # '0'
    trigger_buff_id: int  # 0
    target_select_ai: int  # 1
    is_re_target: int  # 0
    action_id: int  # 400
    skill_duration: str  # '0'
    is_form_action: int  # 1
    skin_action: str  # ''
    skin_name: str  # 'battle_skill_config-510010101'
    buff_id_target: str  # '0'
    buff_id_self: str  # '101:1,1000:1'
    buff_type_target: str  # ''
    buff_type_self: str  # ''
    buff_delay: int  # 0
    description: str  # '提升自身伤害32%,持续3秒。'
    lvup_description: str  # '冷却时间:10秒,伤害提升:32%,持续时间:3秒'
    data_pool_1: str  # '90'
    data_pool_2: str  # '132'
    night_data_pool_1: str  # ''
    night_data_pool_2: str  # ''
    sp_data_pool_1: str  # ''
    sp_data_pool_2: str  # ''
    sppool_trigger_id: str  # ''
    sppool_trigger_type: int  # 0
    sppool_trigger_target: int  # 0
    sppool_trigger_parameter: int  # 0
    sppool_trigger_buff_id: int  # 0
    code: str  # 'powBuffSelf'
    train_coin_type: int  # 1
    train_coin_number: int  # 0
    target_lost: int  # 0
    daynight_only: int  # 0
    interrupt_type: int  # 0
    interrupt_damage_limit: int  # 0
    creation_number: int  # 0
    is_switch: int  # 1
    passive_name: str  # 'battle_skill_config-410010101'
    weight: int  # 0
    consumption: int  # 0
    is_rare: int  # 0
    skill_up_time: int  # 0
    rank: int  # 0
    is_mindupdate: int  # 0
    is_manual: int  # 0
    is_cdr: int  # 1
    skill_lv_call: int  # 1
    special_buff_trigger: str  # '2'
    continue_after_death: int  # 0


class BattleSkillConfig(ConfigTable):
    name = "battle_skill_config"

    def add_instance(self, k):
        skills = []
        for i in range(k * 100 + 1, k * 100 + 11):
            if i not in self._data:
                continue
            modif_stats = {}
            for key, value in self._data[i].items():
                if key == "action_id":
                    value = self.gamedata.battle_action_config[
                        self.gamedata.get_value(value)
                    ]
                elif key == "target_select_ai":
                    value = self.gamedata.battle_target_select_ai[
                        self.gamedata.get_value(value)
                    ]
                elif key == "skin_action":
                    if not value:
                        value = []
                    elif "," not in value:
                        value = [self.gamedata.get_value(value)]
                    else:
                        value = self.gamedata.get_value(value)
                    value = [
                        SkinAction(skin=i, action=self.gamedata.battle_action_config[v])
                        for i, v in value
                    ]
                elif key == "trigger_id":
                    if not value:
                        value = []
                    elif "," not in value:
                        value = [self.gamedata.get_value(value)]
                    else:
                        value = self.gamedata.get_value(value)
                    value = [self.gamedata.battle_trigger[v] for v in value]
                elif key in ["buff_id_target", "buff_id_self"]:
                    if "," not in value:
                        value = [self.gamedata.get_value(value)]
                    else:
                        value = self.gamedata.get_value(value)
                    group = []
                    for i in value:
                        if isinstance(i, list):
                            group.append(
                                BuffTier(
                                    buff=self.gamedata.battle_buff[i[0]], tier=i[1]
                                )
                            )
                        else:
                            group.append(
                                BuffTier(buff=self.gamedata.battle_buff[i], tier=0)
                            )
                    value = group
                else:
                    value = self.gamedata.get_value(value)

                modif_stats[key] = value
            skills.append(BattleSkillConfigInstance(**modif_stats))
        return skills

    def __iter__(self):
        return iter({i["skill_group_id"] for i in self._data.values()})

    def __len__(self):
        return len({i["skill_group_id"] for i in self._data.values()})
