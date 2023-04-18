from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MissionInstance:
    id: int  # 1
    duplicate_type: int  # 0
    coin_type: int  # 0
    campaign: int  # 0
    sub: int  # 1
    if_emergency: int  # 0
    endless_mode: int  # 0
    special_type: int  # 0
    name: str  # '热身运动'
    difficulty: int  # 10000
    exp_parameter: int  # 48
    type: str  # '2'
    enemy_ai_type: int  # 1
    win_turn: int  # 0
    win_spot_id: str  # '7'
    special_spot_id: str  # '6'
    expect_enemy_die_num: int  # 3
    expect_gun_die_num: int  # 0
    expect_turn: int  # 3
    boss_team_id: str  # '222'
    turn_duration: int  # 360000000
    costbp: int  # 0
    getcoin: str  # '0'
    getcoin_parameter: str  # '0'
    coin_ap: int  # 0
    turn_limit: int  # 0
    limit_gun_pool: str  # ''
    limit_team: str  # '0'
    map_res_name: str  # 'Chapter0_1_Y'
    map_information: str  # '4481,4001|2495,1830|-298,-1274'
    is_hide: int  # 0
    is_snow: str  # '0'
    adaptive_gun: str  # ''
    fog_length: str  # ''
    fog_color: str  # ''
    limit_equip_pool: str  # ''
    draw_event_s_id: str  # '0'
    support_available: int  # 2
    enemy_quickmove: int  # 0
    expect_defend_line_turn: int  # 0
    expect_hostage_num: str  # ''
    title_logo: str  # ''
    random_line_spot: str  # '0'
    order: int  # 0
    reinforce_ally_team: str  # '0'
    reinforce_ally_turn: int  # 0
    reinforce_ally_spot: str  # '0'
    ally_boss_team_id: str  # '0'
    ally_code: str  # ''
    supply_parameter: str  # ''
    drop_mission_key: str  # '0'
    close_missions: str  # ''
    mission_group_id: int  # 0
    mission_group_draw_event: str  # ''
    open_mission_keys: str  # ''
    mission_describe: str  # 'mission-20000001'
    force_type: str  # '0'
    round_config: str  # '1:1,2:2,3:3'
    color_change_type: str  # '0'
    color_change_number: str  # '0'
    color_change_result: str  # '0'
    spot_reset: str  # '0'
    draw_code: str  # '0'
    reset_drop_key_once: int  # 0
    close_mission_control: str  # '0'
    limit_squad: int  # -1
    open_mission_items: str  # ''
    drop_mission_item: str  # ''
    mapped_mission_id: int  # 0
    branch_next_mission_id: str  # ''
    win_type: str  # ''
    medal_type_silver: str  # ''
    drop_item_count: str  # ''
    difficulty_recommend: str  # '10000;99'
    difficulty_recommend_addendum: str  # '无妖精需求'
    limit_sangvis: int  # 4
    mission_tip: str  # '推荐编队类型：\n能力均衡编队'
    win_step: str  # ''
    event_score: str  # ''
    score_prize: str  # ''
    drop_key_info: str  # ''
    lose_type: str  # ''
    fight_environment_group: str  # ''
    environment_transform_config: str  # ''


class Mission(ConfigTable):
    name = "mission"

    def add_instance(self, k):
        return MissionInstance(**self._data[k])
