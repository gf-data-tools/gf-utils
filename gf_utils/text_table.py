import logging
from pathlib import Path
import re
from collections.abc import MutableMapping

class TextTable(MutableMapping):
    def __init__(self, table_dir:str):
        self.table_dir = Path(table_dir)
        self.__keys = [p.name[:-4] for p in self.table_dir.glob('*.txt')]
        self.__data = {}

    def __call__(self, key):
        try:
            match = re.fullmatch(r'([a-z][0-9a-z_]+)-([0-9]+)',key)
            table_file = match[1]
            return self[table_file][key]
        except (KeyError,TypeError):
            return key
    
    def __get_text_table(self,table_file):
        table = {}
        logging.debug(f'Reading {table_file}.txt')
        for line in (self.table_dir / f'{table_file}.txt').open('r'):
            key, value = line.strip().split(',',maxsplit=1)
            value = re.sub(r'//c',',',value)
            value = re.sub(r'//n','\n',value)
            table[key] = value.strip()
        return table

    def __getitem__(self, key:str)->str:
        if key not in self.__keys:
            raise KeyError(key)
        if key not in self.__data:
            self.__data[key] = self.__get_text_table(key)
        return self.__data[key]
    
    def __setitem__(self, key, value): raise TypeError('TextTable does not support manual setting')
    def __delitem__(self, key): raise TypeError('TextTable does not support manual deletion')
    def __iter__(self): return iter(self.__keys)
    def __len__(self): return len(self.__keys)
                    

# %%
if __name__=='__main__':
    logging.basicConfig(level='DEBUG',force=True)
    table_dir = r'..\data\us\asset\table'
    table = TextTable(table_dir)
    print(table('battle_skill_config-210040301'))
    print(table('battle_skill_config-211001802'))
    print(table(1234567))


# %%
