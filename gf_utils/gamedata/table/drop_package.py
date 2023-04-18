from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class DropPackageInstance:
    id: int  # 1
    content_ids: str  # ''


class DropPackage(ConfigTable):
    name = "drop_package"

    def add_instance(self, k):
        return DropPackageInstance(**self._data[k])
