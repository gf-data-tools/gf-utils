from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class CarnivalTaskInfoInstance:
    id: str  # '1'
    type: str  # 'cumulative_login'
    count: str  # '1'
    prize_id: str  # '10086'
    title: str  # '累计登录'
    content: str  # '累计登录1天'
    function_control_id: str  # '0'
    carnival_type_id: str  # '1'


class CarnivalTaskInfo(ConfigTable):
    name = "carnival_task_info"

    def add_instance(self, k):
        return CarnivalTaskInfoInstance(**self._data[k])
