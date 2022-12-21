
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class RecommendedFormulaInstance:
    id:int # 1
    develop_type:int # 1
    type:str # '1'
    name:str # '手枪'
    en_name:str # 'HANDGUN'
    content:str # 'recommended_formula-30000001'
    background:str # 'hg_bg'
    mp:int # 130
    ammo:int # 130
    mre:int # 130
    part:int # 30
    type_rarity:str # '1:S,2:D'
    preview:str # '1:1-0,2-0,3-0,5-0,6-0,7-0,8-0,9-0,10-0,11-0,12-0,13-0,14-0,90-0,91-0,96-0,97-0,99-0,100-0,114-0,123-0,126-0,139-0,141-0,168-0,183-0,212-0,233-0,248-0,260-0,269-0,285-0,303-0,310-0,346-0,354-0,375-0|2:16-0,17-0,18-0,21-0,22-0,24-0,25-0,26-0,27-0,31-0,32-0,33-0,92-0,93-0,94-0'
    is_produce:int # 0
    produce_mp:int # 0
    produce_ammo:int # 0
    produce_mre:int # 0
    produce_part:int # 0
    produce_preview:str # ''

class RecommendedFormula(ConfigTable):
    name = 'recommended_formula'

    def add_instance(self,k):
        return RecommendedFormulaInstance(**self._data[k])    
