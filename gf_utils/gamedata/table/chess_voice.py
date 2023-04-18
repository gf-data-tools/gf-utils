from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessVoiceInstance:
    id: int  # 1
    situation: str  # 'jump'
    chip_group: int  # 0
    is_show: int  # 1
    surprise: str  # ''
    code: str  # 'PHRASE'


class ChessVoice(ConfigTable):
    name = "chess_voice"

    def add_instance(self, k):
        return ChessVoiceInstance(**self._data[k])
