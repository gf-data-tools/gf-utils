from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class BondageLinesInstance:
    id: int  # 1
    main_id: str  # 'g:9'
    sub_id: str  # 'g:272'
    lines_code: str  # '||||||||'
    lines_txt: str  # '沙漠之鹰前辈，下次演出你还会来看吗？我想做一些新的尝试！|什么样的尝试？|自从抓住了感觉之后，演出也变得顺利了。但我不想局限在抒情歌曲的舒适区里，还是要挑战高音和摇滚才行。|你的底子不错，P38。不要急着跨出自己的舒适区，先把擅长的东西经营好。|啊……我不该好高骛远的，对，先把擅长的东西练到很优秀才行。嘿嘿……下次您会来听我的歌吗？|我一直在听。|一直在听？|魔女高徒的音乐很不错。你怎么了？|……拜托，前辈，肩膀借给我靠一下，我高兴得要过热了……'


class BondageLines(ConfigTable):
    name = "bondage_lines"

    def add_instance(self, k):
        return BondageLinesInstance(**self._data[k])
