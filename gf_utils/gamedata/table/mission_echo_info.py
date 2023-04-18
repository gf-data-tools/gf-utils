from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MissionEchoInfoInstance:
    id: int  # 1
    mission_id: int  # 10628
    title: str  # '地狱火'
    content: str  # '经历了短暂的希望，ART-556和P7的冒险走到了最后。'
    subtitle: str  # '特工Vector：P7小姐……ART556小姐……$<color=#00BFFF>蒂玛：特工！发生什么事了！</color>$特工Vector：……我们被獠牙发现了。$特工Vector：她击杀了来自格里芬的两位。$<color=#00BFFF>蒂玛：可恶……</color>$<color=#00BFFF>蒂玛：……那你呢？她怎么没有攻击你？</color>$特工Vector：是的，她……她没有攻击我就离开了。$特工Vector：……请求追击。$<color=#00BFFF>蒂玛：嗯，小心行动……你的数据好像有些异常。</color>$<color=#00BFFF>蒂玛：别上她的当。</color>$特工Vector：了解。'
    interval: int  # 3
    character: str  # 'echo_pic1'


class MissionEchoInfo(ConfigTable):
    name = "mission_echo_info"

    def add_instance(self, k):
        return MissionEchoInfoInstance(**self._data[k])
