from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class OrganizationBountyInstance:
    id: int  # 1010001
    org_id: int  # 101
    reward: int  # 21901
    quantity: int  # 5
    organization_level: int  # 2


class OrganizationBounty(ConfigTable):
    name = "organization_bounty"

    def add_instance(self, k):
        return OrganizationBountyInstance(**self._data[k])
