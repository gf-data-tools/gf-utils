from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class DropContentInstance:
    id: int  # 1
    package_id: int  # 945
    content_type: int  # 10
    prize_id: int  # 140006


class DropContent(ConfigTable):
    name = "drop_content"

    def add_instance(self, k):
        return DropContentInstance(**self._data[k])
