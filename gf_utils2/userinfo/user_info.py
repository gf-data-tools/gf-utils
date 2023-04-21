from .gun import GunUserInfo
from .sangvis import SangvisUserInfo
from .squad import SquadUserInfo


class UserInfo(SquadUserInfo, GunUserInfo, SangvisUserInfo):
    pass
