from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class OrganizationLevelInstance:
    id: int  # 101001
    organization_id: int  # 101
    level: int  # 1
    exp: int  # 0
    function_skill_config_id: str  # ''
    description: str  # '初具规模的重要设施，所有部门围绕其运转，发挥着统筹调度的作用。'
    icon: str  # '101_1'


class OrganizationLevel(ConfigTable):
    name = "organization_level"

    def add_instance(self, k):
        return OrganizationLevelInstance(**self._data[k])
