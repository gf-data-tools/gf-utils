from typing import *

from ..gamedata import GameData


class BaseUserInfo:
    def __init__(self, gamedata: GameData, userinfo: Optional[dict] = None):
        self.gamedata = gamedata
        self.__user_info = userinfo

    def __getitem__(self, key):
        return self.__user_info[key]


class BaseGameObject:
    def __init__(self, userinfo: BaseUserInfo) -> None:
        self.userinfo = userinfo
        self.gamedata = userinfo.gamedata
