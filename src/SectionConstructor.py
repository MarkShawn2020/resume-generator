"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 20:50
"""
from typing import TypedDict, Union, List, Optional

from src.LinesConstructor import LinesConstructor
from src.utils import texNode, texBold, texValue, texList


class PeriodItem(TypedDict):
    org: str
    title: str
    period: str
    location: Optional[str]


BaseDetailItem = Union[None, str, List[str]]


class DictDetailItem(TypedDict):
    detail: BaseDetailItem


DetailItem = Union[BaseDetailItem, DictDetailItem]


class SectionConstructor(LinesConstructor):

    def __init__(self, name: str):
        super().__init__()
        self.add(texNode('section', name))

    def addPeriod(self, item: PeriodItem):
        items = [
                texBold(item['org']),
                item['title'],
            ]
        if item.get('location'):
            items.append(item['location'])
        self.add(texNode(
            'datedsubsection',
            COMMA.join(items),
            texValue(item['period'])
        ))

    def addDetail(self, item: DetailItem):
        if not item:
            return
        if isinstance(item, str):
            self.add(item)
        elif isinstance(item, dict):
            self.addDetail(item['detail'])
        elif isinstance(item, list):
            self.add(texList(item))
        else:
            raise ValueError(item)


LANG_ZH = 'zh'
LANG_EN = 'en'
LANG = LANG_ZH
COMMA = '，' if LANG == LANG_ZH else ', '
