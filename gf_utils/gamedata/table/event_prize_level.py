from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EventPrizeLevelInstance:
    id: int  # 1
    name: str  # '镜像论'
    type: int  # 2
    value: str  # '110039'
    condition: str  # '400000:40343;800000:40344;1200000:40345;1600000:40346;2000000:40347;2400000:40348;2800000:40349;3800000:40350;4800000:40351;5800000:40352;7200000:40353;10000000:40354'
    start_time: str  # '2021-01-30 00:00:00'
    end_time: str  # '2021-03-10 23:59:59'
    prize_start_time: str  # '2021-01-30 00:00:00'
    prize_end_time: str  # '2021-03-10 23:59:59'
    left_icon: str  # ''
    background: str  # '7cf3cbf3cd9ba106_draw_210204001.jpg'
    notice_txt: str  # '1、活动期间，在“镜像论”指定积分模式关卡中，累计获取积分，完成积分目标即可领取对应奖励。\n2、每个活动奖励仅可领取一次。\n3、“镜像论”活动结束后将不能继续获取积分，活动界面则会保留至领奖截止时间。\n4、活动界面关闭之前，可从主界面左下角的滚动活动图中进入本领奖界面，活动截止时间结束之后将无法获取奖励。'


class EventPrizeLevel(ConfigTable):
    name = "event_prize_level"

    def add_instance(self, k):
        return EventPrizeLevelInstance(**self._data[k])
