import os
from typing import Iterable
from urllib import request
from urllib.error import URLError
from socket import timeout
import socket
from tqdm.auto import tqdm
from multiprocessing import Pool
from logger_tt import logger

class MultiProcessDownloader:
    def __init__(self,n_jobs:int=16,timeout:float=30,retry:int=10):
        self.n_jobs = n_jobs
        self.timeout = timeout
        self.retry = retry 

    def download(self, tasks:Iterable[Iterable]):
        orig_timeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(self.timeout)

        nj = min(self.n_jobs, len(tasks))
        pool = Pool(nj)
        for task in tasks:
            task.append(self.retry)
        try:
            for _ in tqdm(pool.imap_unordered(download_multitask, tasks),total=len(tasks),ascii=True): 
                pass
        except KeyboardInterrupt as e:
            pool.terminate()
            pool.join()
            raise e
        socket.setdefaulttimeout(orig_timeout)

def download(url, path, max_retry=10):
    fname = os.path.split(path)[-1]
    logger.info(f'Start downloading {fname}')
    for i in range(max_retry):
        try:
            if not os.path.exists(path):
                request.urlretrieve(url,path+'.tmp')
                os.rename(path+'.tmp',path)
        except (URLError, timeout, ConnectionResetError):
            logger.warning(f'Failed to download {fname} for {i+1}/10 tries')
            continue
        else:
            logger.info(f'Successfully downloaded {fname}')
            break
    else:
        logger.error(f'Exceeded max retry times, failed to download {fname} from {url}')
    return path

def download_multitask(x):
    return download(*x)