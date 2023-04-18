from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class BuildingInstance:
    id: int  # 1
    defender: int  # 50
    defender_upper: int  # 50
    belong: int  # 2
    hold_belong: int  # 1
    mission_skill: str  # '0;0;0;0'
    battle_skill: str  # '0;0;405004;0'
    condition: str  # '0:0,1:0;0:0,1:1'
    is_destroy: str  # '1,2'
    is_rebuild: int  # 0
    draw_event: int  # 0
    name: str  # '炮击阵地-普通'
    code: str  # 'MissileLauncher'
    shifting_spot: str  # '4,97'
    shifting_team: str  # '-30,0'
    battle_assist_range: str  # '1,1'
    performance_skill: str  # '800101,102304,405002;0;800101,102304,405002;0'
    show_info: int  # 1
    working_special_spot: str  # ''
    trigger_distance: int  # 0
    active_mission_skill: str  # ''
    inherent_mission_skill: str  # ''
    type: int  # 1
    is_focus: str  # '0'
    transition: str  # ''
    belong_color: str  # '#83CCFF,#FF4646,#FFE683,#C3C3C3'
    working_spot_activation: str  # '1;0'
    active_building_info: str  # 'building-40000001'
    initial_state: int  # 0
    pref_code: str  # ''
    des: str  # '对支援范围内的同归属单位提供战斗支援，战斗中持续对敌方进行炮击打击。'
    confront_des: str  # '本次战役中可采取的应对手段：\n踩点破坏、重装打击'
    squadinfoid: int  # 0
    missionskill_on_death: str  # ''


class Building(ConfigTable):
    name = "building"

    def add_instance(self, k):
        return BuildingInstance(**self._data[k])
