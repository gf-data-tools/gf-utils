from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class FurnitureEstablishInfoInstance:
    establish_id: str  # '10001'
    establish_name: str  # '救助站墙纸'
    room_id: str  # '1'
    description: str  # '救助站墙纸'
    furniture_id: str  # '40001'
    update_furniture_id: str  # '40001'
    furniture_postion: str  # '3,3'
    establish_type: str  # '0'
    establish_lv: str  # '1'
    upgrade_coin: str  # '0'
    upgrade_time: str  # '0'
    upgrade_condition: str  # '0'
    parameter_1: str  # ''
    parameter_2: str  # ''
    parameter_3: str  # ''


class FurnitureEstablishInfo(ConfigTable):
    name = "furniture_establish_info"

    def add_instance(self, k):
        return FurnitureEstablishInfoInstance(**self._data[k])
