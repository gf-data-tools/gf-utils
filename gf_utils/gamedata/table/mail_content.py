from ._base import ConfigTable
from dataclasses import dataclass


@dataclass
class MailContentInstance:
    id: int  # 1
    title: str  # '测试邮件'
    content: str  # '这是一封测试关卡解锁的邮件，解锁1-4后您会收到这封邮件，邮件持续至活动结束时间。'


class MailContent(ConfigTable):
    name = "mail_content"

    def add_instance(self, k):
        return MailContentInstance(**self._data[k])
