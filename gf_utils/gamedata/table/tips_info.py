
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class TipsInfoInstance:
    id:str # '1'
    title:str # 'tips_TeamLabelDrag(Clone)'
    regTarget:str # 'Formation://Canvas'
    targetPath:str # 'Formation://Canvas/Formation/Left/Scroller/Team/TeamLabelDrag(Clone)'
    tipsManagePath:str # 'Formation://Canvas/Top/TopBackground/TipsManage'
    tipsID:str # '选择<color=#e57006>梯队</color> 提供更多战斗选择'
    bg_path:str # 'Tips/Tips_BG_Right'
    tipPos:str # '222,0,0'
    tipSize:str # '244,250'

class TipsInfo(ConfigTable):
    name = 'tips_info'

    def add_instance(self,k):
        return TipsInfoInstance(**self._data[k])    
