# %%
import json
from collections.abc import MutableMapping
from pathlib import Path

from logger_tt import logger

from .text_table import TextTable

# %%
special_keys = {
    "achievement": "identity",
    "attendance_info": None,
    "auto_mission": "mission_id",
    "bingo_task_info": "task_id",
    "chess_creation_logic": None,
    "daily_info": "identity",
    "daily": "identity",
    "enemy_standard_attribute": "level",
    "equip_category": "category",
    "equip_exp_info": "level",
    "equip_type": "type",
    "furniture_establish_info": "establish_id",
    "game_config_info": "parameter_name",
    "guild_level": "lv",
    "gun_exp_info": "lv",
    "gun_obtain_info": "obtain_id",
    "kalina_favor_info": "level",
    "main_quest_info": "identity",
    "mission_draw_bonus": None,
    "mission_event_prize_info": "mission_id",
    "mission_targettrain_battlesetting": "difficult_level",
    "sangvis_advance": "lv",
    "sangvis_exp": "lv",
    "seven_attendance_info": None,
    "seven_spendpoint_info": None,
    "squad_chip_exp": "lv",
    "squad_exp": "lv",
    "squad_rank": "star_id",
    "squad_type": "type_id",
    "weekly_info": "identity",
    "weekly": "identity",
}


class GameData(MutableMapping):
    def __init__(self, stc_dir, table_dir=None, to_dict=True) -> None:
        self.stc_dir = Path(stc_dir)
        self.text_table = TextTable(table_dir) if table_dir else lambda x: x
        self.to_dict = to_dict
        self.__keys = [p.name[:-5] for p in self.stc_dir.glob("*.json")]
        self.__data = {}

    def __get_stc_dict(self, name):
        logger.debug(f"Reading {name}.json")
        with (self.stc_dir / f"{name}.json").open("r", encoding="utf-8") as f:
            data = json.load(f)
            data = convert_text(data, self.text_table)
            if self.to_dict and len(data) > 0:
                k = (
                    "id"
                    if "id" in data[0].keys()
                    else (special_keys[name] if name in special_keys.keys() else None)
                )
                if k is not None:
                    data = {d[k]: d for d in data}
        return data

    def __getitem__(self, key):
        if key not in self.__keys:
            raise KeyError(key)
        if key not in self.__data:
            self.__data[key] = self.__get_stc_dict(key)
        return self.__data[key]

    def __getattr__(self, k):
        return self[k]

    def __call__(self, k):
        return self[k]

    def __setitem__(self, key, value):
        raise TypeError("GameData object does not support __setitem__")

    def __delitem__(self, key):
        raise TypeError("GameData object does not support __setitem__")

    def __iter__(self):
        return iter(self.__keys)

    def __len__(self):
        return len(self.__keys)


def convert_text(data, text_table):
    if type(data) == list:
        return [convert_text(i, text_table) for i in data]
    elif type(data) == dict:
        return {k: convert_text(v, text_table) for k, v in data.items()}
    else:
        text = text_table(data)
        if text != "":
            return text
        else:
            return data


# %%
if __name__ == "__main__":
    import os

    from logger_tt import setup_logging

    cfg = setup_logging(log_path=os.devnull)
    cfg.root_handlers[0].setLevel("DEBUG")

    table_dir = R"..\GF_Data_Tools\data\ch\asset\table"
    stc_dir = R"..\GF_Data_Tools\data\ch\stc"
    stc = GameData(stc_dir, table_dir)
    stc["achievement"]
# %%
