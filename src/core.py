"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 18:40
"""
import json
import os.path

from mergedeep import merge

from src.SectionConstructor import SectionConstructor
from src.LinesConstructor import LinesConstructor
from src.settings import SECTION_NAME_MAP, OVERLOAD_DATA, RENDER_SEPARATOR_LR, \
    RENDER_SEPARATOR_L, \
    RENDER_ITEMS, PART_SPECIAL, PART_SIMPLE_SECTIONS, PART_PERIOD_SECTIONS, PROJECT_DIR, TEX_SRC_DIR
from src.utils import texNode


def generateResumeTex(fp: str):
    with open(fp, 'r') as f:
        data = dict(merge(json.load(f), OVERLOAD_DATA))

    collector = LinesConstructor()
    for render_item in RENDER_ITEMS:  # type: str
        if RENDER_SEPARATOR_LR not in render_item:
            render_item += RENDER_SEPARATOR_LR
        _path, _choices = render_item.rsplit(RENDER_SEPARATOR_LR, 1)
        part = _path.rsplit(RENDER_SEPARATOR_L, 1)[-1]
        _data = data.copy()
        for _path in _path.split(RENDER_SEPARATOR_L):
            _data = _data[_path]
        if _choices:
            _data = [_data[key] for key in _choices.split(",")]
        if part in PART_SPECIAL:
            item = texNode(part, *_data)
        elif part in PART_SIMPLE_SECTIONS:
            item = SectionConstructor(SECTION_NAME_MAP[part])
            item.addDetail(_data)
        elif part in PART_PERIOD_SECTIONS:
            item = SectionConstructor(SECTION_NAME_MAP[part])
            for line in _data:  # type: dict
                item.addPeriod(line)
                item.addDetail(line)
        else:
            raise ValueError(part)
        collector.add(item)

    fn = os.path.basename(fp).rsplit('.', 1)[0]
    collector.output(os.path.join(TEX_SRC_DIR, f'{fn}.tex'))
