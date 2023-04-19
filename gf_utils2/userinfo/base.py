from typing import *

from ..gamedata import GameData


class BaseUserInfo:
    def __init__(self, gamedata: GameData, userinfo: Optional[dict] = None):
        self.gamedata = gamedata
        self.raw = userinfo

    def __getitem__(self, key):
        return self.raw[key]


class BaseGameObject:
    gamedata = None
    userinfo = None

    @staticmethod
    def set_gamedata(gamedata: GameData):
        BaseGameObject.gamedata = gamedata
        BaseGameObject.userinfo = BaseUserInfo(gamedata)

    @property
    def gamedata(self):
        return self.userinfo.gamedata

    def __init__(self, userinfo: BaseUserInfo | None = None, **kwargs) -> None:
        if userinfo is not None:
            self.userinfo = userinfo
        for k, v in kwargs.items():
            setattr(self, k, v)
