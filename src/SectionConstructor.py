"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 20:50
"""
from typing import TypedDict, Union, List

from src.LinesConstructor import LinesConstructor
from src.settings import COMMA
from src.utils import texNode, texBold, texValue, texList


class PeriodItem(TypedDict):
    org: str
    title: str
    period: str


BaseDetailItem = Union[None, str, List[str]]


class DictDetailItem(TypedDict):
    detail: BaseDetailItem


DetailItem = Union[BaseDetailItem, DictDetailItem]


class SectionConstructor(LinesConstructor):

    def __init__(self, name: str):
        super().__init__()
        self.add(texNode('section', name))

    def addPeriod(self, item: PeriodItem):
        self.add(texNode(
            'datedsubsection',
            COMMA.join([
                texBold(item['org']),
                item['title'],
            ]),
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
