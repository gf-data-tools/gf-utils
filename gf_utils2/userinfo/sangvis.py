from __future__ import annotations

from bisect import bisect
from dataclasses import dataclass
from functools import cached_property, partial
from math import ceil, floor
from typing import *

from .base import BaseGameObject, BaseUserInfo

SangvisAttr = Literal[
    "hp", "pow", "rate", "hit", "dodge", "armor", 
    "armor_piercing", "crit", "crit_dmg"
]  # fmt:skip


class SangvisUserInfo(BaseUserInfo):
    @cached_property
    def sangvis_with_user_info(self) -> dict[int, Sangvis]:
        return {
            int(k): Sangvis(v, self) for k, v in self["sangvis_with_user_info"].items()
        }


@dataclass(init=False)
class Sangvis(BaseGameObject):
    id: int = 0
    user_id: int = 0
    sangvis_id: int = 1001
    sangvis_exp: int = 0
    sangvis_level: int = 0
    sangvis_advance: int = 0
    sangvis_resolution: int = 0
    sangvis_resolution_level: int = 0
    sangvis_shape_n: int = 0
    sangvis_is_special: int = 0
    skill1: int = 0
    skill2: int = 0
    skill3: int = 0
    skill_advance: int = 0
    chip1: int = 0
    chip2: int = 0
    can_click: int = 0
    favor: int = 0
    favor_toplimit: int = 0
    max_favor: int = 0
    life: int = 0
    sign: int = 0
    soul_bond: int = 0
    soul_bond_time: int = 0
    skin: int = 0
    special_effect: int = 0
    is_locked: int = 0

    def __init__(
        self, record: dict, userinfo: BaseUserInfo | None = None, **kwargs
    ) -> None:
        super().__init__(userinfo, **kwargs)
        for k, v in record.items():
            setattr(self, k, int(v))
        self.sangvis_info = self.gamedata["sangvis"][self.sangvis_id]

    def attr(
        self, attr: SangvisAttr, max_favor: bool = False, max_advance: bool = False
    ) -> int:
        sangvis_info = self.sangvis_info
        gamedata = self.gamedata
        advance = 5 if max_advance else self.sangvis_advance

        match attr:
            case "hp" | "pow" | "rate" | "hit" | "dodge" | "armor":
                size_coef = [100, 100, 102, 105, 108, 110][self.sangvis_shape_n]
                eat_ratio = sangvis_info["eat_ratio"]
                attr_ratio = sangvis_info[f"ratio_{attr}"]
                advance_ratio = gamedata["sangvis_advance"][advance][f"advance_{attr}"]
                level_ratio = self.sangvis_level + 39
                type_basic = gamedata["sangvis_type"][sangvis_info["type"]][
                    f"basic_{attr}"
                ]

                base_value = (
                    size_coef
                    * eat_ratio
                    * attr_ratio
                    * advance_ratio
                    * level_ratio
                    * type_basic
                    / 1e8
                )

                resolution = gamedata["sangvis_resolution"][
                    sangvis_info["resolution"] * 100 + self.sangvis_resolution
                ]
                assert resolution["group_id"] == sangvis_info["resolution"]
                assert resolution["lv"] == self.sangvis_resolution
                resolution_value = resolution[f"resolution_{attr}"]

                if attr == "hp" or attr == "pow":
                    formation_value = ceil(base_value / sangvis_info["formation"])
                else:
                    formation_value = ceil(base_value)
                resolution_value = formation_value + resolution[f"resolution_{attr}"]

                if attr == "hp":
                    number = min(
                        sangvis_info["formation"], self.sangvis_resolution_level + 1
                    )
                    return resolution_value * number

                if attr in ["pow", "hit", "dodge"]:
                    favor = self.favor / 10000
                    if max_favor:
                        favor = 150 if self.soul_bond else 100
                    favor_factor = bisect([10, 90, 140, 190], favor) * 0.05 + 0.95
                    return ceil(resolution_value * favor_factor)

                return resolution_value

            case "armor_piercing" | "crit" | "crit_dmg":
                return sangvis_info[attr]

            case _:
                raise ValueError(f"Unsupported attr {attr}")

    def battle_efficiency(self, max_favor=False, max_advance=False, night=False):
        # Raised (Split Number * Soldier Coefficient *
        # (Dead Speed Coefficient * (Firepower + Iron Armor/3) *
        # (Fatality Rate * (Fatal Wound - 1) + 1) * Hit / (Hit +23) + 8))
        get_attr = partial(self.attr, max_favor=max_favor, max_advance=max_advance)
        sangvis_info = self.sangvis_info

        number = min(sangvis_info["formation"], self.sangvis_resolution_level + 1)
        hit = get_attr("hit")
        if night:
            hit = hit / 10
        atk_effi = ceil(
            (5 * number)
            * (
                (get_attr("rate") / 50)
                * (get_attr("pow") + get_attr("armor_piercing") / 3)
                * (get_attr("crit") / 100 * (get_attr("crit_dmg") / 100 - 1) + 1)
                * (hit / (hit + 23))
                + 8
            )
        )
        # Raise (Health * (35 + Dodge)/35 * (2.6 * 200/(200 - Gloves) - 1.6))
        def_effi = ceil(
            get_attr("hp")
            * ((35 + get_attr("dodge")) / 35)
            * (2.6 * 200 / max(1, 200 - get_attr("armor")) - 1.6)
        )
        # Rounded (Fraction * (0.8 + Origin Grade/5) * (35 + (5 * (Skill Level -1))))
        # Rounded (Fraction * (0.8 + Origin Grade/5) * (15 + (2 * (Skill Level -1))))
        skill_lv = (self.skill1, self.skill2, self.skill3, self.skill_advance)
        rank = sangvis_info["rank"] - 2
        skl_effi = ceil(number * (0.8 + rank / 5) * (30 + 5 * skill_lv[0]))
        for lv in skill_lv[1:]:
            print(skl_effi)
            if lv == 0:
                continue
            skl_effi += ceil(number * (0.8 + rank / 5) * (13 + 2 * lv))

        res_effi = 200 if self.sangvis_resolution else 0

        print(f"{atk_effi=} {def_effi=} {skl_effi=} {res_effi=}")
        return atk_effi + def_effi + skl_effi + res_effi
