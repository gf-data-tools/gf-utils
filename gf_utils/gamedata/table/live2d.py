from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class Live2dInstance:
    id: int  # 1
    motions: str  # '1000,1001\n,1002\n,1003\n,1004\n,1005\n,1006\n,1007\n,1008\n,1009\n,1010\n,1011\n,1012\n,1013\n,1014\n,1015\n,1016\n,1017\n,1018\n,1019\n,1020\n,1021\n,1022\n,1023\n,1024\n,1025\n,1026\n,1027\n,1028\n,1029\n,1030\n,1031\n,1032\n,1033\n,1034\n,1035\n,1036\n,1037\n,1038\n,1039\n,1040\n,1041\n,1042\n,1043\n,1044\n,1045\n,1046\n,1047\n,1048\n,1049\n,1050\n,1051\n,1052\n,1053\n,1054\n,1055\n,1056\n,1057\n,1058\n,1059\n,1060\n,1061\n,1062\n,1063\n,1064\n,1065\n,1066\n,1067\n,1068\n,1069\n,1070\n,1071\n,1072\n,1073\n,1074\n,1075\n,1076\n,1077\n,1078\n,1079\n,1080\n,1081\n,1082,1083'
    code: str  # 'NPC_Kalina'
    fit_gun: int  # -1
    skin: int  # 0
    mail_offset_x: str  # ''
    mail_offset_y: str  # ''
    mail_scale: str  # ''
    skinType: int  # 1
    skinLogo: int  # 1
    fit_sangvis: int  # 0
    is_show: int  # 1


class Live2d(ConfigTable):
    name = "live2d"

    def add_instance(self, k):
        return Live2dInstance(**self._data[k])
