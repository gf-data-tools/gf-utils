from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class ChessChipTargetSelectInstance:
    id: int  # 1
    target_type: str  # '9'
    target_number: int  # 1
    is_select: int  # 0
    range: str  # ''
    select_order: str  # '1'
    select_limit: int  # 0
    select_type: int  # 1


class ChessChipTargetSelect(ConfigTable):
    name = "chess_chip_target_select"

    def add_instance(self, k):
        return ChessChipTargetSelectInstance(**self._data[k])
