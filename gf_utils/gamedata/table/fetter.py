from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FetterInstance:
    id: int  # 1
    name: str  # '成为耀眼之人吧'
    actor: str  # 'g:9;g:167;g:92;g:7;g:272'
    code: str  # 'C121'
    milestone1: int  # 50
    milestone1_reward: str  # 'p:23001'
    milestone2: int  # 120
    milestone2_reward: str  # 'p:23002'
    milestone3: int  # 250
    milestone3_reward: str  # 'p:23003'
    milestone4: int  # 400
    milestone4_reward: str  # 'p:23004'
    milestone5: int  # 500
    milestone5_reward: str  # 'p:23005'


class Fetter(ConfigTable):
    name = "fetter"

    def add_instance(self, k):
        return FetterInstance(**self._data[k])
