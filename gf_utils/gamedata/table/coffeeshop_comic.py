from dataclasses import dataclass

from ._base import ConfigTable


@dataclass
class CoffeeshopComicInstance:
    id: str  # '1'
    title: str  # '官方四格-第一章'
    description: str  # '作者：AC130'
    cost: str  # '506-600'
    prize_id: str  # '5004'
    item_ids: str  # '0'


class CoffeeshopComic(ConfigTable):
    name = "coffeeshop_comic"

    def add_instance(self, k):
        return CoffeeshopComicInstance(**self._data[k])
