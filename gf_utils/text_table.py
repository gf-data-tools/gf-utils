import logging
from pathlib import Path
import re
import csv

class TextTable:
    def __init__(self, table_dir:str):
        self.table_dir = Path(table_dir)
        self.tables = {}
        self.keys = [fpath.name.split('.')[0] for fpath in self.table_dir.glob('*.txt')]

    def __call__(self, k):
        return self[k]
    
    def __getitem__(self, k:str)->str:
        try:
            if k in self.tables:
                return self.tables[k]
            match = re.fullmatch(r'([a-z][0-9a-z_]+)-([0-9]+)',k)
            table_file = match[1]
            if table_file in self.keys:
                return k
            else:
                logging.debug(f'Reading {table_file}.txt')
                for line in (self.table_dir / f'{table_file}.txt').open('r'):
                    key, value = line.split(',',maxsplit=1)
                    value = re.sub(r'//c',',',value)
                    value = re.sub(r'//n','\n',value)
                    self.tables[key] = value.strip()
                return self.tables[k]
        except (TypeError, KeyError, FileNotFoundError, ValueError):
            return k
                    

# %%
if __name__=='__main__':
    logging.basicConfig(level='DEBUG',force=True)
    table_dir = r'..\data\us\asset\table'
    table = TextTable(table_dir)
    print(table('battle_skill_config-210040301'))
    print(table('battle_skill_config-211001802'))
    print(table(1234567))


# %%
