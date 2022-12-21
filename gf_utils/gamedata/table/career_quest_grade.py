
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class CareerQuestGradeInstance:
    id:int # 1
    group:int # 2
    grade:int # 11
    name:str # '轻锐小队'
    description:str # '纵然是一颗小小的星火，亦有照亮无边黑暗的雄心壮志。'

class CareerQuestGrade(ConfigTable):
    name = 'career_quest_grade'

    def add_instance(self,k):
        return CareerQuestGradeInstance(**self._data[k])    
