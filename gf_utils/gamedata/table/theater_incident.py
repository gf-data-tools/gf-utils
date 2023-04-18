from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class TheaterIncidentInstance:
    id: int  # 1
    name: str  # '渗透侦查'
    description: str  # '需要对敌方占领的区域进行渗透侦查'
    icon: str  # 'TheaterIncident1'
    type: int  # 1
    timing: int  # 1
    scout_selection_id: str  # '101,102,103'
    scout_majority_coef: int  # 50
    scout_manority_coef: int  # 200
    is_active: int  # 1
    theater_event_id: int  # 9


class TheaterIncident(ConfigTable):
    name = "theater_incident"

    def add_instance(self, k):
        return TheaterIncidentInstance(**self._data[k])
