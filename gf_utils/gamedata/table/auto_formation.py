from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class AutoFormationInstance:
    id: int  # 1
    name: str  # '能力均衡编队'
    sangvis_id: int  # 0
    description: str  # '<color=#ff7f00>突击步枪</color>与<color=#ff7f00>冲锋枪</color>的常规编队，拥有平衡的能力。'
    reco_location: str  # '1:4,2:4,3:4,5:2,6:2'
    reco_gun_1: str  # '60,20060,62,20065,65,72,118,119,130,175,187,194,196,206,216,262,274,289,314,58,68,70,71,74,105,107,108,133,134,170,193,265,279,313,342,356,361,365,20293,372,378'
    reco_gun_2: str  # '54,20055,55,20056,56,20057,57,20061,61,20065,65,66,106,122,20122,171,172,206,207,214,236,237,274,287,288,290,318,293,297,306,133,105,71,138,193,223,239,279,298,73,1027,20171,378'
    reco_gun_3: str  # '56,20056,20057,57,20061,61,62,20064,64,20065,65,66,69,72,118,119,122,20122,129,172,175,181,187,194,196,205,207,214,215,227,236,237,243,262,289,314,290,318,293,74,107,120,138,170,223,239,258,265,1007,338,342,361,20205,378'
    reco_gun_4: str  # ''
    reco_gun_5: str  # '16,23,20026,26,28,20029,29,20031,31,20032,32,59,20093,93,20101,101,102,20103,103,104,115,127,135,137,143,20143,150,213,224,225,228,245,315,286,304,18,19,22,24,25,33,116,144,178,191,218,1019,267,291,1023,359,20104,20115'
    reco_gun_6: str  # '20,28,20029,29,20032,32,59,20093,93,20094,94,20101,101,20103,103,115,135,136,177,203,213,234,245,315,251,259,280,295,304,17,18,21,22,27,92,116,169,176,131,191,209,218,267,311,333,347'
    reco_gun_7: str  # ''
    reco_gun_8: str  # ''
    reco_gun_9: str  # ''


class AutoFormation(ConfigTable):
    name = "auto_formation"

    def add_instance(self, k):
        return AutoFormationInstance(**self._data[k])
