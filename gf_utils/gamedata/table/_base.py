from collections.abc import MutableMapping
from abc import abstractmethod
from dataclasses import dataclass
from logger_tt import logger


@dataclass
class SkillArg:
    major: int = 1
    minor: int = 1


@dataclass
class BuffTier:
    buff: int
    tier: int


class ConfigTable(MutableMapping):
    @property
    @abstractmethod
    def name():
        return "name"

    def __init__(self, gamedata):
        self.gamedata = gamedata
        self._data = self.gamedata[self.name]
        self._instance = {}

    def __getitem__(self, k):
        if not isinstance(k, int):
            return k
        elif k == 0:
            return k
        if k not in self._instance:
            try:
                self._instance[k] = self.add_instance(k)
            except KeyError as e:
                logger.exception(f"{self.name} does not have {k}")
                self._instance[k] = k
        return self._instance[k]

    @abstractmethod
    def add_instance(self, k):
        return None

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)
