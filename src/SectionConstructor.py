"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 20:50
"""
from src.LinesConstructor import LinesConstructor
from src.settings import COMMA
from src.utils import texNode, texBold, texValue, texList


class SectionConstructor(LinesConstructor):

    def __init__(self, name: str):
        super().__init__()
        self.add(texNode('section', name))

    def addPeriod(self, where: str, role: str, period: str):
        self.add(texNode(
            'datedsubsection',
            COMMA.join([
                texBold(where),
                role,
            ]),
            texValue(period)
        ))

    def addDetail(self, detail):
        if not detail:
            return
        if isinstance(detail, str):
            self.add(detail)
        elif isinstance(detail, list):
            self.add(texList(detail))
        else:
            raise ValueError(detail)
