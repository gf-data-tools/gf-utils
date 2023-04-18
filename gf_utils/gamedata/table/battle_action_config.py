from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BattleActionConfigInstance:
    id: int  # 1
    name: str  # '普通攻击'
    action_order: str  # '1'
    action_delay: str  # '0'
    action_playspeed: str  # '100'
    creation_order: str  # '1'
    creation_delay: str  # '0'
    creation_afterdeath: str  # ''
    sound_order: str  # ''
    sound_delay: str  # ''
    effect_order: str  # ''
    effect_delay: str  # ''
    effect_duration: str  # ''
    stop_time_speed: str  # ''
    stop_time_delay: str  # ''
    stop_time_duration: str  # ''
    move_order: str  # ''
    move_delay: str  # ''
    summon_order: str  # ''
    summon_delay: str  # ''
    voice_order: str  # ''
    voice_delay: str  # ''
    scene_order: str  # ''
    scene_play_speed: str  # ''
    scene_delay: str  # ''
    scene_transition: str  # ''
    avg_order: str  # ''
    avg_delay: str  # ''
    bgm_order: str  # ''
    bgm_delay: str  # ''
    camera_order: str  # ''
    camera_delay: str  # ''
    camera_duration: str  # ''


class BattleActionConfig(ConfigTable):
    name = "battle_action_config"

    def add_instance(self, k):
        modif_stats = {}
        for key, value in self._data[k].items():
            # if key=='action_order':
            #     if ',' not in value:
            #         value = [self.gamedata.get_value(value)]
            #     else:
            #         value = self.gamedata.get_value(value)
            #     value = [self.gamedata.battle_action_config[i] for i in value]
            if key == "creation_order":
                if "," not in value:
                    value = [self.gamedata.get_value(value)]
                else:
                    value = self.gamedata.get_value(value)
                value = [self.gamedata.battle_creation[i] for i in value]
            elif key == "move_order":
                if "," not in value:
                    value = [self.gamedata.get_value(value)]
                else:
                    value = self.gamedata.get_value(value)
                value = [self.gamedata.battle_movement_info[i] for i in value]
            else:
                value = self.gamedata.get_value(value)

            modif_stats[key] = value
        return BattleActionConfigInstance(**modif_stats)
