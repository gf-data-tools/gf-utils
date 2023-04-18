from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class BingoTaskInfoInstance:
    task_id: str  # '1'
    type: str  # 'general'
    task_name: str  # 'mission_common_win'
    size: str  # '3'
    ticket_num: str  # '1'
    title: str  # '普通战役挑战'
    content: str  # '战斗胜利情况下挑战任意普通战役3次'
    is_mutex: str  # '1'
    function_control_id: str  # '0'
    task_type_id: str  # '1'


class BingoTaskInfo(ConfigTable):
    name = "bingo_task_info"

    def add_instance(self, k):
        return BingoTaskInfoInstance(**self._data[k])
