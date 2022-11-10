"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 19:14
"""
from typing import List

from src.LinesConstructor import LinesConstructor


def texValue(value):
    return '{' + value + '}'


def texNode(name, *values):
    s = '\\' + name

    for value in values:
        s += texValue(value)
    return s


def texBold(value):
    return texNode('textbf', value)


def texItalic(value):
    return texNode('textit', value)


def texList(vs: List[str]) -> LinesConstructor:
    ls = LinesConstructor()
    ls.add(r'\begin{itemize}[parsep=0.2ex]')
    for v in vs:
        ls.add(texNode('item', v))
    ls.add(r'\end{itemize}')
    return ls
