from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class EventBattlepassInstance:
    id: int  # 1
    name: str  # 'BattlePass_1_1.png;BattlePass_1_2.png'
    pt_item_id: int  # 10606
    gift_free: str  # '1:110001,3:110002,5:110003,6:110004,8:110005,10:110006,12:110007,14:110008,15:110009,17:110010,19:110011,21:110012,23:110013,25:110014,26:110015,28:110016,30:110017,31:110018,33:110019,34:110020,35:110021,36:110022,38:110023,40:110024,42:110025,44:110026,45:110027'
    gift_paytounlock: str  # '1:120001,2:120002,3:120003,4:120004,5:120005,6:120006,7:120007,8:120008,9:120009,10:120010,11:120011,12:120012,13:120013,14:120014,15:120015,16:120016,17:120017,18:120018,19:120019,20:120020,21:120021,22:120022,23:120023,24:120024,25:120025,26:120026,27:120027,28:120028,29:120029,30:120030,31:120031,32:120032,33:120033,34:120034,35:120035,36:120036,37:120037,38:120038,39:120039,40:120040,41:120041,42:120042,43:120043,44:120044,45:120045'
    gift_plus: str  # '130003'
    gift_extra: int  # 130001
    start_time: str  # '2022-08-29 00:00:00'
    end_time: str  # '2022-10-02 23:59:59'
    skin_id: str  # '57_30001'
    paid_productid: str  # 'cn_test:272,273,274;cn_appstore:372,373,374;cn_mica:472,473,474;cn_alpha:572,573,574;cn_dev:672,673,674;cn_txy:772,773,774;cn_bili:872,873,874;cn_third:972,973,974;cn_check:3037,3038,3039'
    paid_productid_discount: str  # 'cn_test:272,273,274;cn_appstore:372,373,374;cn_mica:472,473,474;cn_alpha:572,573,574;cn_dev:672,673,674;cn_txy:772,773,774;cn_bili:872,873,874;cn_third:972,973,974;cn_check:3037,3038,3039'
    exp_mallid: int  # 35
    discount_itemid: int  # 160001
    exhibit_bonus: str  # '130002,130003'
    unlock_itemid: str  # '140001;140002'


class EventBattlepass(ConfigTable):
    name = "event_battlepass"

    def add_instance(self, k):
        return EventBattlepassInstance(**self._data[k])
