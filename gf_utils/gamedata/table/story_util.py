from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class StoryUtilInstance:
    id: int  # 1
    mission_id: str  # '1'
    description: str  # 'M4A1报告:AR小组之前受帕斯卡委托，潜入S09区回收一个名为“莱柯”的人类留下的资料。'
    scripts: str  # '0-1-1,0-1-2'
    campaign: int  # 0
    bgm: str  # 'BGM_Frontline'
    title: str  # '热身运动'
    is_util: int  # 1
    start: str  # '0-1-1'
    round: str  # ''
    point: str  # ''
    first: str  # '0-1-2'
    mid: str  # ''
    end: str  # '0-1-2'
    fail: str  # ''
    step_start_story: str  # ''
    step_end_story: str  # ''


class StoryUtil(ConfigTable):
    name = "story_util"

    def add_instance(self, k):
        return StoryUtilInstance(**self._data[k])
