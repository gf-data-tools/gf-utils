import os
import socket
from functools import partial
from multiprocessing.pool import Pool, ThreadPool
from socket import timeout
from typing import Iterable
from urllib import request
from urllib.error import URLError

from logger_tt import logger
from tqdm.auto import tqdm


class MultiProcessDownloader:
    def __init__(self, n_jobs: int = 16, timeout: float = 30, retry: int = 10):
        self.n_jobs = n_jobs
        self.timeout = timeout
        self.retry = retry
        self.pool = Pool(n_jobs)

    def download(self, tasks: Iterable[Iterable]):
        for task in tasks:
            task.append(self.retry)
            task.append(self.timeout)
        try:
            for _ in tqdm(
                self.pool.imap_unordered(download_multitask, tasks),
                total=len(tasks),
                ascii=True,
            ):
                pass
        except KeyboardInterrupt as e:
            self.pool.terminate()
            self.pool.join()
            raise e


def download(url, path, max_retry=10, timeout_sec=30):
    path = str(path)
    socket.setdefaulttimeout(timeout_sec)
    fname = os.path.split(path)[-1]
    logger.info(f"Start downloading {fname} from {url}")
    for i in range(max_retry):
        try:
            if not os.path.exists(path):
                req = request.Request(url, headers={"User-Agent": ""})
                resp = request.urlopen(req)
                with open(path + ".tmp", "wb") as f:
                    f.write(resp.read())
                os.rename(path + ".tmp", path)
        except (URLError, timeout, ConnectionResetError):
            logger.warning(f"Failed to download {fname} for {i+1}/10 tries")
            continue
        else:
            logger.info(f"Successfully downloaded {fname}")
            break
    else:
        logger.error(f"Exceeded max retry times, failed to download {fname} from {url}")
    return path


class Downloader:
    def __init__(self, n_jobs: int = 16, timeout: float = 30, retry: int = 10):
        self.pool = ThreadPool(n_jobs)
        self.retry = retry
        self.timeout = timeout

    def download(self, tasks: Iterable[Iterable]):
        download_func = partial(
            download, max_retry=self.retry, timeout_sec=self.timeout
        )
        try:
            for _ in tqdm(
                self.pool.imap_unordered(lambda t: download_func(*t), tasks),
                total=len(tasks),
                ascii=True,
            ):
                pass
        except KeyboardInterrupt as e:
            self.pool.terminate()
            self.pool.join()
            raise e


def download_multitask(x):
    return download(*x)
