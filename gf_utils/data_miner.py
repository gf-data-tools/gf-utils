# %%
import pyjson5
import json
import logging
import os
import io
import shutil
from urllib import request
from .download import download
from .crypto import get_des_encrypted, get_md5_hash, xor_decrypt
from .asset_extractor import unpack_all_assets
from .format_stc import format_stc
import base64
import re
import gzip
from gzip import GzipFile
from zipfile import ZipFile
import argparse
from gf_utils.stc_data import get_stc_data
import traceback
from logger_tt import logger


hosts = {
    'us': {
        'game_host': 'http://gf-game.sunborngame.com/index.php/1001',
        'cdn_host': 'http://gfus-cdn.sunborngame.com',
        'asset_host': 'http://gfus-cdn.sunborngame.com',
    },
    'jp': {
        'game_host': 'http://gfjp-game.sunborngame.com/index.php/1001',
        'cdn_host': 'http://gfjp-cdn.sunborngame.com',
        'asset_host': 'http://gfjp-cdn.sunborngame.com',
    },
    'kr': {
        'game_host': 'http://gf-game.girlfrontline.co.kr/index.php/1001',
        'cdn_host': 'http://gfkrcdn.imtxwy.com',
        'asset_host': 'http://sn-list.girlfrontline.co.kr',
    },
    'tw': {
        'game_host': 'http://sn-game.txwy.tw/index.php/1001',
        'cdn_host': 'http://sncdn.imtxwy.com',
        'asset_host': 'http://sn-list.txwy.tw',
    },
    'ch': {
        'game_host': 'http://gfcn-game.gw.merge.sunborngame.com/index.php/1000',
        'cdn_host': 'http://gf-cn.cdn.sunborngame.com',
        'asset_host': 'http://gf-cn.cdn.sunborngame.com',
    },
}

# %%
class DataMiner():
    def __init__(self,region='ch',raw_root='raw',data_root='data'):
        self.region=region
        self.host = hosts[region]
        self.res_key = 'kxwL8X2+fgM='
        self.res_iv = 'M9lp+7j2Jdwqr+Yj1h+A'
        self.lua_key = 'lvbb3zfc3faa8mq1rx0r0gl61b4338fa'
        self.dat_key = 'c88d016d261eb80ce4d6e41a510d4048'
        self.raw_dir = os.path.join(raw_root,region)
        self.data_dir = os.path.join(data_root,region)
        for dir in [self.raw_dir, self.data_dir]:
            os.makedirs(dir,exist_ok=True)
        self.get_current_version()
        

    def get_current_version(self):
        version_url = self.host['game_host'] + '/Index/version'
        logger.info(f'requesting version from {version_url}')
        response = request.urlopen(version_url)
        version = pyjson5.loads(response.read().decode())
        self.version = version
        self.dataVersion = version["data_version"]
        self.clientVersion = version["client_version"]
        self.minversion = round(eval(self.clientVersion)/100) * 10
        self.abVersion = version["ab_version"]
        logger.info(f'client {self.clientVersion} | ab {self.abVersion} | data {self.dataVersion}')

    def get_res_data(self):
        bkey = base64.standard_b64decode(self.res_key)
        biv = base64.standard_b64decode(self.res_iv)
        fname = f"{self.minversion}_{self.abVersion}_AndroidResConfigData"

        en = get_des_encrypted(fname,bkey,biv[:8])
        res_config = base64.standard_b64encode(en).decode('utf-8')
        res_config = re.sub(r"[^a-zA-Z0-9]","",res_config)+'.txt'
        resdata_url = self.host['asset_host']+'/'+res_config
        resdata_fp = os.path.join(self.raw_dir,'AndroidResConfigData')
        download(resdata_url,resdata_fp)
        unpack_all_assets(resdata_fp,self.raw_dir)
        with open(os.path.join(self.raw_dir,'assets/resources/resdata.asset'),encoding='utf-8') as f:
            self.resdata = pyjson5.load(f)
        shutil.copy(os.path.join(self.raw_dir,'assets/resources/resdata.asset'),os.path.join(self.data_dir,'resdata.json'))

    def get_asset_bundles(self):
        res_url = self.resdata['resUrl']
        targets = ['asset_textavg','asset_texttable','asset_textes']
        for ab_info in self.resdata['BaseAssetBundles']:
            if ab_info['assetBundleName'] in targets:
                ab_url = f'{res_url}{ab_info["resname"]}.ab'
                ab_fp = os.path.join(self.raw_dir,f'{ab_info["assetBundleName"]}.ab')
                download(ab_url,ab_fp)

    def get_stc(self):
        hash = get_md5_hash(self.dataVersion)
        stc_url = self.host['cdn_host'] + "/data/stc_" + self.dataVersion + hash + ".zip"
        stc_fp = os.path.join(self.raw_dir,'stc.zip')
        download(stc_url,stc_fp)
        ZipFile(stc_fp).extractall(os.path.join(self.raw_dir,'stc'))
    
    def update_raw_resource(self, force=False):
        available = False
        if not force:
            saved_version_fp = os.path.join(self.data_dir,'version.json')
            if not os.path.exists(saved_version_fp):
                available = True
            else:
                with open(saved_version_fp,encoding='utf-8') as f:
                    version = pyjson5.load(f)
                if version["data_version"] != self.dataVersion:
                    available =True
        else:
            available = True

        if available:
            for dir in [self.raw_dir, self.data_dir]:
                if os.path.exists(dir):
                    shutil.rmtree(dir)
                os.makedirs(dir)
            logger.info('new data available, start downloading')
            self.get_res_data()
            self.get_asset_bundles()
            self.get_stc()
            self.process_assets()
            self.process_catchdata()
            self.process_stc()
            self.format_json()
            with open(os.path.join(self.data_dir,'version.json'),'w',encoding='utf-8') as f:
                json.dump(self.version,f,indent=4,ensure_ascii=False)
            shutil.rmtree(self.raw_dir)
        else:
            logger.info('current data is up to date')
        return available
        
    def process_assets(self):
        for asset in ['asset_textavg','asset_texttable','asset_textes']:
            unpack_all_assets(os.path.join(self.raw_dir,asset+'.ab'),self.raw_dir)
        asset_output = os.path.join(self.data_dir,'asset')
        os.makedirs(asset_output,exist_ok=True)
        asset_dir = os.path.join(self.raw_dir,'assets/resources/dabao')
        for subdir in os.listdir(asset_dir):
            shutil.copytree(os.path.join(asset_dir,subdir),os.path.join(asset_output,subdir),dirs_exist_ok=True)
        self.decode_luapatch()

    def decode_luapatch(self):
        src_dir = os.path.join(self.data_dir,'asset/luapatch')
        for root,dirs,files in os.walk(src_dir):
            for file in files:
                if not file.endswith('txt'):
                    continue
                logger.info(f'decoding {file}')
                with open(os.path.join(root,file),'rb') as f:
                    cipher = f.read()
                plain = xor_decrypt(cipher,self.lua_key)
                with open(os.path.join(root,file[:-4]),'wb') as f:
                    f.write(plain)
                os.remove(os.path.join(root,file))
    
    def decode_catchdata(self,cipher):
        logger.info(f'decoding catchdata')
        compressed = xor_decrypt(cipher,self.dat_key)
        plain = gzip.decompress(compressed).decode('utf-8')
        # plain = GzipFile(fileobj=io.BytesIO(compressed)).read().decode('utf-8')
        return plain
    
    def encode_catchdata(self,plain:str):
        logger.info(f'encoding catchdata')
        compressed = gzip.compress(plain.encode('utf-8'))
        cipher = xor_decrypt(compressed,self.dat_key)
        return cipher

    def process_catchdata(self):
        dst_dir = os.path.join(self.data_dir,'catchdata')
        os.makedirs(dst_dir,exist_ok=True)
        with open(os.path.join(self.raw_dir,'stc/catchdata.dat'),'rb') as f:
            cipher = f.read()
        plain=self.decode_catchdata(cipher)
        with open(os.path.join(dst_dir,'catchdata'),'w',encoding='utf-8') as f:
            f.write(plain)
        for json_string in plain.split('\n')[:-1]:
            data = json.loads(json_string)
            assert len(data.keys()) == 1
            for key in data.keys():
                logger.info(f'Formatting {key}.json from catchdata')
                with open(os.path.join(dst_dir,f'{key}.json'),'w',encoding='utf-8') as f:
                    json.dump(data[key],f,indent=4,ensure_ascii=False)
        
    def process_stc(self):
        mapping_dir = os.path.join('conf/stc-mapping',str(self.minversion))
        logger.info(f'Read stc-mapping from {mapping_dir}')
        stc_dir = os.path.join(self.raw_dir,'stc')
        dst_dir = os.path.join(self.data_dir,'stc')
        os.makedirs(dst_dir,exist_ok=True)

        for f in os.listdir(mapping_dir):
            id, ext = os.path.splitext(f)
            assert ext=='.json'
            stc = os.path.join(stc_dir,f'{id}.stc')
            mapping = os.path.join(mapping_dir,f'{id}.json')
            name, data = format_stc(stc,mapping)
            with open(os.path.join(dst_dir, f'{name}.json'),'w',encoding='utf-8') as f:
                json.dump(data,f,indent=4,ensure_ascii=False)

    def format_csv(self):
        output_dir = os.path.join(self.data_dir,'csv') 
        os.makedirs(output_dir,exist_ok=True)
        table_dir = os.path.join(self.data_dir,'asset/table')
        for j in ['catchdata','stc']:
            json_dir = os.path.join(self.data_dir,j)
            data = get_stc_data(json_dir, table_dir,to_dict=False)
            for key, value in data.items():
                pd.DataFrame.from_records(value).to_csv(os.path.join(output_dir,f'{key}.csv'),index=False)

    def format_json(self):
        output_dir = os.path.join(self.data_dir,'json_with_text') 
        os.makedirs(output_dir,exist_ok=True)
        table_dir = os.path.join(self.data_dir,'asset/table')
        for j in ['catchdata','stc']:
            json_dir = os.path.join(self.data_dir,j)
            data = get_stc_data(json_dir, table_dir,to_dict=False)
            for key, value in data.items():
                with open(os.path.join(output_dir,f'{key}.json'),'w',encoding='utf-8') as f:
                    json.dump(value,f,ensure_ascii=False,indent=4)


# %%
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('region',nargs='+',choices=['ch','tw','kr','jp','us'])
    parser.add_argument('--force', '-f',action='store_true')
    args=parser.parse_args()
    for region in args.region:
        try:
            logger.basicConfig(level='INFO',format=f'%(asctime)s %(levelname)s: [{region.upper()}] %(message)s',force=True)
            data_miner = DataMiner(region)
            data_miner.update_raw_resource(args.force)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(f"Extraction failed due to {e}")
# %%
