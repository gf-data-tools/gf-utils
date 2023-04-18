from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FunctionSkillConfigInstance:
    id: int  # 101
    name: str  # '搜索理论'
    level: int  # 1
    group_id: int  # 0
    code: str  # 'function_skill_icon_101'
    description: str  # '作战任务的报酬有 {0}% 概率增加一次额外掉落{1}'
    arguments: int  # 3
    max_level: int  # 5
    is_show: int  # 1
    type: int  # 1
    function_skill: str  # 'extra_drop_rate_up'


class FunctionSkillConfig(ConfigTable):
    name = "function_skill_config"

    def add_instance(self, k):
        return FunctionSkillConfigInstance(**self._data[k])
