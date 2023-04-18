from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FetterStoryInstance:
    id: int  # 101
    fetter_id: int  # 1
    actor: str  # 'g:9'
    milestone: int  # 0
    reward: int  # 22006
    name: str  # '朴素的魔女'
    description: str  # '“珍珠蒙尘，亦是珍珠。”'


class FetterStory(ConfigTable):
    name = "fetter_story"

    def add_instance(self, k):
        return FetterStoryInstance(**self._data[k])
