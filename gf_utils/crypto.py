import base64
import io
import time
from gzip import GzipFile

from Crypto.Cipher import ARC4, DES
from Crypto.Hash import MD5
from Crypto.Util.Padding import pad


def get_md5_hash(input: str):
    data = MD5.MD5Hash(input.encode("utf-8")).digest()
    return ("{:02x}" * len(data)).format(*data)


def get_des_encrypted(data, key, iv):
    des = DES.new(key=key, iv=iv, mode=DES.MODE_CBC)
    return des.encrypt(pad(data.encode("utf-8"), block_size=des.block_size))


def xor_decrypt(cipher, key):
    key = key.encode("utf-8")
    lk = len(key)
    plain = [c ^ key[i % lk] for i, c in enumerate(cipher)]
    return bytes(plain)


def decrypt_rc4(data, key):
    rc4 = ARC4.new(key)
    return rc4.decrypt(data)


def request_decrypt(src, key):
    hash = get_md5_hash(key)
    righthash = get_md5_hash(hash[16:])
    rc4Key = righthash + get_md5_hash(righthash)
    while len(src) % 4 != 0:
        src += "="
    cipher = base64.standard_b64decode(src)
    plain = decrypt_rc4(cipher, rc4Key.encode("utf-8"))
    return plain


def request_decode(src, key="yundoudou"):
    if src[0] == "#":
        compressed = request_decrypt(src[1:], key)
        plain = GzipFile(fileobj=io.BytesIO(compressed[26:])).read().decode("utf-8")
    else:
        plain = request_decrypt(src, key)
    return plain


def request_encrypt(src, key):
    hash = get_md5_hash(key)
    righthash = get_md5_hash(hash[16:])
    rc4Key = righthash + get_md5_hash(righthash)
    cipher = decrypt_rc4(src, rc4Key.encode("utf-8"))
    cipher = base64.standard_b64encode(cipher)
    return cipher


def request_encode(src, key="yundoudou", timeout=3600, expire=None):
    if expire is None:
        expire = str(int(time.time()) + timeout)
    hash = get_md5_hash(key)
    lefthash = get_md5_hash(hash[:16])
    srchash = get_md5_hash(src + lefthash)[:16]
    plain = expire + srchash + src
    return request_encrypt(plain.encode("utf-8"), key)
