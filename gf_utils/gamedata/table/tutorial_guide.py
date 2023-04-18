from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TutorialGuideInstance:
    id: int  # 100
    type: int  # 1
    child_ids: str  # '101,102,103,104,105,106'
    title: str  # '基础战术'
    title_code: str  # 'guide_intermediate'
    sub_title: str  # '指挥作战的基本要领，学会这些内容后再让您的梯队出发吧'
    tutorial_manual_id: int  # 0
    rank: int  # 0


class TutorialGuide(ConfigTable):
    name = "tutorial_guide"

    def add_instance(self, k):
        return TutorialGuideInstance(**self._data[k])
