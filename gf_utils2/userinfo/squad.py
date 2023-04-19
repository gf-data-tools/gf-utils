from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import *

from .base import BaseGameObject, BaseUserInfo


class SquadUserInfo(BaseUserInfo):
    @property
    def squad_with_user_info(self) -> dict[int, Squad]:
        return {int(k): Squad(self, v) for k, v in self["squad_with_user_info"].items()}

    @property
    def chip_with_user_info(self) -> dict[int, Chip]:
        return {int(k): Chip(self, v) for k, v in self["chip_with_user_info"].items()}


@dataclass(init=False)
class Squad(BaseGameObject):
    id: int = 0
    squad_id: int = 0
    squad_exp: int = 0
    squad_level: int = 0
    rank: int = 0
    advanced_level: int = 0
    life: int = 0
    cur_def: int = 0
    ammo: int = 0
    mre: int = 0
    assist_damage: int = 0
    assist_reload: int = 0
    assist_hit: int = 0
    assist_def_break: int = 0
    damage: int = 0
    atk_speed: int = 0
    hit: int = 0
    def_: int = 0
    skill1: int = 0
    skill2: int = 0
    skill3: int = 0

    def __init__(self, userinfo: SquadUserInfo, record: dict) -> None:
        super().__init__(userinfo)
        for k, v in record.items():
            if k == "def":
                k = "def_"
            setattr(self, k, int(v))
        self.squad_info = self.gamedata["squad"][self.squad_id]
        self.chips = [
            chip
            for chip in userinfo.chip_with_user_info.values()
            if chip.squad_with_user_id == self.id
        ]

    def assist_attr(
        self,
        attr: Literal["damage", "def_break", "hit", "reload"],
        max_eat: bool = True,
        include_chip: bool = True,
    ) -> int:
        attr_name = f"assist_{attr}"
        attr_id = {"damage": 1, "def_break": 2, "hit": 3, "reload": 4}[attr]
        gamedata = self.gamedata

        squad = self.squad_info
        squad_std_attr = gamedata["squad_standard_attribution"][attr_id]
        squad_type = gamedata["squad_type"][squad["type"]]
        squad_rank = gamedata["squad_rank"][self.rank]

        basic_ratio = (
            squad[attr_name]
            * squad["basic_rate"]
            * squad_std_attr["standard_attribute"]
            * squad_std_attr["basic_rate"]
            * squad_type[attr_name]
            * 1e-6
        )
        if not max_eat:
            basic_value = ceil(basic_ratio * 0.5 + getattr(self, attr_name))
        else:
            basic_value = ceil(basic_ratio * (49 + self.squad_level) / 100)
            for advance in gamedata["squad_advanced_bonus"].values():
                if (
                    advance["group_id"] == squad["advanced_bonus"]
                    and advance["lv"] == self.advanced_level
                ):
                    basic_value += advance[attr_name]

        if not include_chip:
            return basic_value

        chip_max = ceil(
            squad[attr_name]
            * squad["cpu_rate"]
            * squad_std_attr["standard_attribute"]
            * squad_std_attr["cpu_rate"]
            * squad_type[attr_name]
            * squad_rank["cpu_rate"]
            * (49 + 100)
            * 1e-10
        )
        chip_value = min(chip_max, sum(chip.assist_attr(attr) for chip in self.chips))

        cpu_bonus = gamedata["squad_cpu"][squad["cpu_id"]]["cpu_bonus"]
        bonus_grid = sum(chip.chip_info["grid_number"] for chip in self.chips)
        bonus_value = sum(
            bonus[attr_name]
            for bonus in gamedata["squad_cpu_completion"].values()
            if bonus["group_id"] == cpu_bonus and bonus["unlock_number"] <= bonus_grid
        )

        return basic_value + chip_value + bonus_value

    def battle_efficiency(
        self,
        max_eat: bool = True,
        include_chip: bool = True,
    ) -> int:
        damage, def_break, hit, reload = [
            self.assist_attr(k, max_eat, include_chip)
            for k in ["damage", "def_break", "hit", "reload"]
        ]

        # 破防效能=破防*范围系数/100*精度/(精度+23*8)*(300+装填)/1500*14
        db_effi = (
            def_break
            * (self.squad_info["display_assist_area_coef"] / 100)
            * (hit / (hit + 23 * 8))
            * ((300 + reload) / 1500)
            * 14
        )
        # 杀伤效能=(杀伤+穿甲/2)*范围系数/100*精度/(精度+23*8)*(300+装填)/1500*((暴击伤害/100-1)*暴击/100+1)*48
        dmg_effi = (
            (damage + self.squad_info["armor_piercing"] / 2)
            * (self.squad_info["display_assist_area_coef"] / 100)
            * (hit / (hit + 23 * 8))
            * ((300 + reload) / 1500)
            * (
                (self.squad_info["crit_damage"] / 100 - 1)
                * (self.squad_info["crit_rate"] / 100)
                + 1
            )
            * 48
        )
        # 技能效能=90+30*技能等级
        skl_effi = 270 + (self.skill1 + self.skill2 + self.skill3) * 30

        return ceil(db_effi + dmg_effi + skl_effi)


@dataclass(init=False)
class Chip(BaseGameObject):
    id: int = 0
    user_id: int = 0
    chip_id: int = 0
    chip_exp: int = 0
    chip_level: int = 0
    color_id: int = 0
    grid_id: int = 0
    squad_with_user_id: int = 0
    position: tuple[int, int] = (0, 0)
    shape_info: tuple[int, int] = (0, 0)
    assist_damage: int = 0
    assist_reload: int = 0
    assist_hit: int = 0
    assist_def_break: int = 0
    damage: int = 0
    atk_speed: int = 0
    hit: int = 0
    def_: int = 0
    is_locked: int = 0

    def __init__(self, userinfo: SquadUserInfo, record: dict[str, str]) -> None:
        super().__init__(userinfo)
        for k, v in record.items():
            if k == "def":
                k = "def_"
            if k in ["position", "shape_info"]:
                setattr(self, k, tuple([int(i) for i in v.split(",")]))
            else:
                setattr(self, k, int(v))
        self.chip_info = self.gamedata["squad_chip"][self.chip_id]

    def assist_attr(
        self,
        attr: Literal["damage", "def_break", "hit", "reload"],
    ) -> int:
        attr_name = f"assist_{attr}"
        attr_id = {"damage": 1, "def_break": 2, "hit": 3, "reload": 4}[attr]

        cpu_std_attr = self.gamedata["squad_standard_attribution"][attr_id][
            "cpu_standard_attribute"
        ]
        intensity_ratio = self.gamedata["squad_chip"][self.chip_id]["intensity_ratio"]
        nb_grid = getattr(self, attr_name)

        base_value = ceil(cpu_std_attr * intensity_ratio * nb_grid / 100)

        level_coef = (
            self.gamedata["squad_chip_exp"][self.chip_level]["strength_coef"]
            if self.chip_level > 0
            else 100
        )

        return ceil(base_value * level_coef / 100)
