"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 20:52
"""
from __future__ import annotations
from typing import List


class LinesConstructor:

    def __init__(self):
        self._lines = []

    @property
    def data(self) -> List[str]:
        return self._lines

    @property
    def docData(self) -> str:
        items = [
            r'\documentclass{resume}'
            r'\begin{document}'
        ]
        if not PAGE_NUMBERING_VISIBILITY:
            items.append(r'\pagenumbering{gobble} % suppress displaying page number')
        items.extend(self.data)
        items.append(r'\end{document}')
        return '\n\n'.join(items)

    def add(self, v) -> LinesConstructor:
        if isinstance(v, str):
            self._lines.append(v)
        elif isinstance(v, LinesConstructor):
            self._lines.extend(v.data)
        else:
            raise ValueError
        return self

    def addBefore(self, v) -> LinesConstructor:
        self._lines.insert(0, v)
        return self

    def output(self, fp: str):
        if not fp.endswith('.tex'):
            raise ValueError(f'{fp} should endswith .tex')
        with open(fp, 'w') as f:
            print(f'writing file://{fp}')
            f.write(self.docData)


PAGE_NUMBERING_VISIBILITY = False
