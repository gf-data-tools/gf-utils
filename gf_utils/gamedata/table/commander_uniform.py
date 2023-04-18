from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class CommanderUniformInstance:
    id: int  # 1010
    name: str  # '防毒面具'
    description: str  # '即使在末日也不能放弃自己，顺便在里面敷个面膜吧。'
    code: str  # 'Head'
    icon: str  # 'commander_1010_icon'
    type: int  # 1
    gender: int  # 0
    uniform_class: str  # '10'
    color_normal: str  # 'Commander_02_initial_a_1'
    color_0: str  # ''
    color_1: str  # ''
    color_2: str  # ''
    color_3: str  # ''
    color_4: str  # ''
    skill_id: int  # 0
    bone_name: str  # ''
    rotation: int  # 0
    scale: float  # 0.0
    position: str  # ''
    color_icon_id: str  # '1'


class CommanderUniform(ConfigTable):
    name = "commander_uniform"

    def add_instance(self, k):
        return CommanderUniformInstance(**self._data[k])
