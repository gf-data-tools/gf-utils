import re
from collections.abc import MutableMapping
from pathlib import Path

from logger_tt import logger


class TextTable(MutableMapping):
    def __init__(self, table_dir: str | Path):
        self.table_dir = Path(table_dir)
        self.__keys = [p.name[:-4] for p in self.table_dir.glob("*.txt")]
        self.__data = {}

    def __call__(self, key):
        try:
            match = re.fullmatch(r"([a-z][0-9a-z_]+)-([0-9]+)", key)
            table_file = match[1]
            return self[table_file][key]
        except (KeyError, TypeError):
            return key

    def __get_text_table(self, table_name):
        table = {}
        table_path = self.table_dir / f"{table_name}.txt"
        logger.debug(f"Loading {table_name}.txt")
        for lineno, line in enumerate(table_path.open("r", errors="ignore")):
            try:
                key, value = line.strip().split(",", maxsplit=1)
                value = re.sub(R"//c", ",", value)
                value = re.sub(R"//n", "\n", value)
                table[key] = value.strip()
            except Exception as e:
                logger.error(f"{repr(e)} in {table_path}:{lineno}")
                logger.debug("", exc_info=True)
        return table

    def __getitem__(self, key: str) -> str:
        if key not in self.__keys:
            raise KeyError(key)
        if key not in self.__data:
            self.__data[key] = self.__get_text_table(key)
        return self.__data[key]

    def __setitem__(self, key, value):
        raise TypeError("TextTable object does not support __setitem__")

    def __delitem__(self, key):
        raise TypeError("TextTable object does not support __setitem__")

    def __iter__(self):
        return iter(self.__keys)

    def __len__(self):
        return len(self.__keys)


# %%
if __name__ == "__main__":
    import os

    from logger_tt import setup_logging

    cfg = setup_logging(log_path=os.devnull)
    cfg.root_handlers[0].setLevel("DEBUG")

    table_dir = R"..\GF_Data_Tools\data\ch\asset\table"
    table = TextTable(table_dir)

    print(table("prize-10000070"))
    print(table("battle_skill_config-211001802"))
    print(table("1234"))
    print(table(1234567))


# %%
