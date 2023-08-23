from __future__ import annotations

from bisect import bisect
from dataclasses import dataclass
from functools import cached_property, partial
from math import ceil, floor
from typing import *

from .base import BaseGameObject, BaseUserInfo

EquipAttrs = Literal[
    "pow", "hit", "dodge", "speed", "rate", "critical_harm_rate", "critical_percent",
    "armor_piercing", "armor", "shield", "damage_amplify", "damage_reduction",
    "night_view_percent", "bullet_number_up", "skill_effect_per", "skill_effect"
]  # fmt:skip


GunAttrs = Literal[
    "life", "bullet_number", "night_view_percent", 
    "critical_percent", "critical_harm_rate", "armor_piercing", 
    "pow", "hit", "dodge", "rate", "armor", "speed", "skill_effect_per", "skill_effect"
]  # fmt:skip


def gf_ceil(number):
    if number % 1 < 0.0001:
        number = number - (number % 1)
    else:
        number = number - (number % 1) + 1
    return int(number)


class GunUserInfo(BaseUserInfo):
    @cached_property
    def gun_with_user_info(self) -> dict[int, Gun]:
        return {int(i["id"]): Gun(i, self) for i in self["gun_with_user_info"]}

    @cached_property
    def equip_with_user_info(self) -> dict[int, Equip]:
        return {int(k): Equip(v, self) for k, v in self["equip_with_user_info"].items()}


@dataclass(init=False)
class Equip(BaseGameObject):
    id: int = 0
    user_id: int = 0
    gun_with_user_id: int = 0
    equip_id: int = 0
    equip_exp: int = 0
    equip_level: int = 0
    pow: int = 0
    hit: int = 0
    dodge: int = 0
    speed: int = 0
    rate: int = 0
    critical_harm_rate: int = 0
    critical_percent: int = 0
    armor_piercing: int = 0
    armor: int = 0
    shield: int = 0
    damage_amplify: int = 0
    damage_reduction: int = 0
    night_view_percent: int = 0
    bullet_number_up: int = 0
    adjust_count: int = 0
    is_locked: int = 0
    last_adjust: dict[str, int]

    def __init__(
        self, record: dict[str, str] = {}, userinfo: GunUserInfo = None, **kwargs
    ) -> None:
        self.last_adjust = {}
        super().__init__(userinfo, **kwargs)
        for k, v in record.items():
            if k == "last_adjust":
                if v.startswith("{"):
                    setattr(self, k, eval(v))
                else:
                    setattr(self, k, {})
            else:
                setattr(self, k, int(v))
        self.equip_info = self.gamedata["equip"][self.equip_id]

    def attr(self, attr: EquipAttrs, max_adjust=False) -> int:
        equip_info = self.equip_info
        if attr.startswith("skill"):
            return equip_info[attr]
        if equip_info[attr] == "":
            return 0

        adj_min, adj_max = (int(i) for i in equip_info[attr].split(","))
        adj_val = getattr(self, attr) if not max_adjust else 10000
        base_value = round((adj_min * (10000 - adj_val) + adj_max * adj_val) / 10000)

        bonus_coef = {
            s.split(":")[0]: int(s.split(":")[1])
            for s in equip_info["bonus_type"].split(",")
            if equip_info["bonus_type"]
        }.get(attr, 0)
        lv = self.equip_level

        value = floor(base_value * (1 + bonus_coef * lv / 10000))

        return value


@dataclass(init=False)
class Gun(BaseGameObject):
    id: int = 0
    user_id: int = 0
    gun_id: int = 1
    gun_exp: int = 0
    gun_level: int = 0
    team_id: int = 0
    if_modification: int = 0
    location: int = 0
    position: int = 0
    life: int = 0
    ammo: int = 0
    mre: int = 0
    pow: int = 0
    hit: int = 0
    dodge: int = 0
    rate: int = 0
    skill1: int = 0
    skill2: int = 0
    fix_end_time: int = 0
    is_locked: int = 0
    number: int = 0
    equip1: int = 0
    equip2: int = 0
    equip3: int = 0
    equip4: int = 0
    favor: int = 0
    max_favor: int = 0
    favor_toplimit: int = 0
    soul_bond: int = 0
    skin: int = 0
    can_click: int = 0
    soul_bond_time: int = 0
    special_effect: int = 0

    def __init__(
        self, record: dict = {}, userinfo: GunUserInfo | None = None, **kwargs
    ) -> None:
        super().__init__(userinfo, **kwargs)
        for k, v in record.items():
            setattr(self, k, int(v))
        self.gun_info = self.gamedata["gun"][self.gun_id]
        self.equips: list[Equip] = []
        if userinfo is not None:
            equip_with_user_info = userinfo.equip_with_user_info
            if self.equip1 != 0:
                self.equips.append(equip_with_user_info[self.equip1])
            if self.equip2 != 0:
                self.equips.append(equip_with_user_info[self.equip2])
            if self.equip3 != 0:
                self.equips.append(equip_with_user_info[self.equip3])

    def equip_attr(self, attr: EquipAttrs, max_adjust: bool = False):
        return sum(equip.attr(attr, max_adjust) for equip in self.equips)

    def attr(
        self,
        attr: GunAttrs,
        max_eat: bool = False,
        max_favor: bool = False,
        max_adjust=False,
    ) -> int:
        gamedata = self.gamedata
        gun_info = self.gun_info
        game_config = gamedata["game_config_info"]
        equip_attr = partial(self.equip_attr, max_adjust=max_adjust)

        match attr:
            case "pow" | "hit" | "dodge" | "rate":
                type_ratio = float(
                    gamedata["gun_type_info"][str(self.gun_info["type"])][
                        f"basic_attribute_{attr}"
                    ]
                )
                gun_ratio = gun_info[f"ratio_{attr}"]
                gun_eat_ratio = gun_info[f"eat_ratio"]

                attr_ = attr if attr != "pow" else "power"

                basic_str = game_config[f"{attr_}_basic"]["parameter_value"]
                basic, _ = (float(i) for i in basic_str.split(","))
                basic_value = ceil(basic * type_ratio * gun_ratio / 100)

                if max_eat:
                    grow_str = game_config[
                        f"{attr_}_grow{'_after100' if self.gun_level>100 else''}"
                    ]["parameter_value"]
                    grow_inc, _, _, grow_base = (float(i) for i in grow_str.split(","))
                    grow_value = ceil(
                        (grow_base + grow_inc * (self.gun_level - 1))
                        * (type_ratio * gun_ratio * gun_eat_ratio / 10000)
                    )
                else:
                    grow_value = getattr(self, attr)

                gun_value = basic_value + grow_value
                if attr != "rate":
                    if max_favor:
                        if self.soul_bond == 0:
                            favor = 100
                        elif self.if_modification == 0:
                            favor = 150
                        else:
                            favor = 200
                    else:
                        favor = self.favor // 10000
                    favor_factor = bisect([10, 90, 140, 190], favor) * 0.05 + 0.95
                    gun_value = gf_ceil(gun_value * favor_factor)

                equip_value = equip_attr(attr)
                return gun_value + equip_value
            case "life" | "armor":
                type_ratio = float(
                    gamedata["gun_type_info"][str(self.gun_info["type"])][
                        f"basic_attribute_{attr}"
                    ]
                )
                gun_ratio = gun_info[f"ratio_{attr}"]

                basic_str = game_config[
                    f"{attr}_basic{'_after100' if self.gun_level>100 else''}"
                ]["parameter_value"]
                basic_base, basic_inc, _ = (float(i) for i in basic_str.split(","))

                gun_value = ceil(
                    (basic_base + basic_inc * (self.gun_level - 1))
                    * (type_ratio * gun_ratio / 100)
                )
                if attr == "life":
                    return gun_value * self.number

                equip_value = equip_attr(attr)
                return gun_value + equip_value
            case "night_view_percent" | "critical_harm_rate" | "skill_effect_per" | "skill_effect":
                fix_value = 0
                if attr == "critical_harm_rate":
                    fix_value = 150
                return equip_attr(attr) + fix_value
            case "armor_piercing" | "critical_percent" | "bullet_number":
                attr1 = attr2 = attr
                if attr == "critical_percent":
                    attr2 = "crit"
                if attr == "bullet_number":
                    attr1 = "bullet_number_up"
                    attr2 = "special"
                return equip_attr(attr1) + gun_info[attr2]
            case "speed":
                type_speed = float(
                    gamedata["gun_type_info"][str(self.gun_info["type"])][
                        f"basic_attribute_{attr}"
                    ]
                )
                return equip_attr(attr) + type_speed * 10
            case "rec":
                type_ratio = float(
                    gamedata["gun_type_info"][str(self.gun_info["type"])][
                        f"basic_attribute_rec"
                    ]
                )
                gun_ratio = gun_info[f"ratio_{attr}"]

                basic_str = game_config[f"gun_rec_basic"]["parameter_value"]
                basic_base, basic_inc, _ = (float(i) for i in basic_str.split(","))

                gun_value = ceil(
                    (basic_base + basic_inc * (self.gun_level - 1))
                    * (type_ratio * gun_ratio / 100)
                )

                return gun_value

            case _:
                raise ValueError(f"Unsupported attr {attr}")

    def battle_efficiency(
        self,
        night=False,
        max_eat: bool = False,
        max_favor: bool = False,
        max_adjust: bool = False,
    ):
        gun_attr = partial(
            self.attr, max_eat=max_eat, max_favor=max_favor, max_adjust=max_adjust
        )
        gun_info = self.gun_info

        dmg_factor = (gun_attr("pow") + gun_attr("armor_piercing") / 3) * (
            1
            + (gun_attr("critical_percent") / 100)
            * (gun_attr("critical_harm_rate") / 100 - 1)
        )
        if not night:
            hit = gun_attr("hit")
        else:
            # 夜战命中 = CEILING(命中*(1+(-0.9*(1-夜视仪数值/100))),1)
            hit = gf_ceil(
                gun_attr("hit") * (0.1 + 0.9 * gun_attr("night_view_percent") / 100)
            )
        hit_factor = hit / (hit + 23)

        match gun_info["type"]:
            case 6:
                # SG攻击 = 6*5*(3*弹量*(伤害+穿甲/3)*(1+暴击率*(暴击伤害-100)/10000)/(1.5+弹量*50/射速+0.5*弹量)*命中/(命中+23)+8)
                type_factor = 6
                rate_factor = gun_attr("bullet_number") / (
                    1.5 + gun_attr("bullet_number") * (50 / gun_attr("rate") + 0.5)
                )
            case 5:
                # MG攻击 = 7*5*((伤害+穿甲/3)*(1+暴击率*(暴击伤害-100)/10000)*弹量/(弹量/3+4+200/射速)*命中/(命中+23)+8)
                type_factor = 7
                rate_factor = gun_attr("bullet_number") / (
                    gun_attr("bullet_number") / 3 + 4 + 200 / gun_attr("rate")
                )
            case _:
                # 其他攻击 = 5*5*(伤害+穿甲/3)*(1+暴击率*(暴击伤害-100)/10000)*射速/50*命中/(命中+23)+8)
                type_factor = 5
                rate_factor = gun_attr("rate") / 50
        atk_effi = gf_ceil(
            type_factor * self.number * (dmg_factor * rate_factor * hit_factor + 8)
        )

        # 防御效能 = CEILING(生命*(35+闪避)/35*(4.2*100/MAX(1,100-护甲)-3.2),1)
        dodge_factor = (35 + gun_attr("dodge")) / 35
        armor_factor = 4.2 * 100 / max(1, 100 - gun_attr("armor")) - 3.2
        def_effi = gf_ceil(
            (gun_attr("life") * 0.9 + gun_attr("rec") * 0.5 * 5)
            * dodge_factor
            * armor_factor
        )
        # 1技能效能 = ceiling（5*(0.8+星级/10)*[35+5*(技能等级-1)]*(100+skill_effect_per)/100,1) + skill_effect
        # 2技能效能 = ceiling（5*(0.8+星级/10)*[15+2*(技能等级-1)]*(100+skill_effect_per)/100,1) + skill_effect
        skl1_effi = gf_ceil(
            self.number
            * (0.8 + gun_info["rank"] / 10)
            * (30 + 5 * self.skill1)
            * (1 + gun_attr("skill_effect_per") / 100)
            + gun_attr("skill_effect")
        )
        skl2_effi = gf_ceil(
            self.number
            * (0.8 + gun_info["rank"] / 10)
            * (13 + 2 * self.skill1)
            * (1 + gun_attr("skill_effect_per") / 100)
        )
        skl_effi = (skl1_effi if self.skill1 else 0) + (skl2_effi if self.skill2 else 0)

        return atk_effi + def_effi + skl_effi
