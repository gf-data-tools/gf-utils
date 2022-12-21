from collections.abc import MutableMapping
from abc import abstractmethod


class ConfigTable(MutableMapping):
    @property 
    @abstractmethod
    def name(): return 'name'

    def __init__(self, gamedata):
        self.gamedata = gamedata
        self._data = self.gamedata[self.name]
    
    @abstractmethod
    def __getitem__(self, k): return None
    def __setitem__(self, key, value): raise NotImplementedError()
    def __delitem__(self, key): raise NotImplementedError()
    def __iter__(self): return iter(self._data)
    def __len__(self): return len(self._data)