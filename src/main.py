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
from src.settings import DATA_DIR, PROJECT_DIR, SECTION_MAP, OVERLOAD_DATA, RENDER_SEPARATOR_LR, RENDER_SEPARATOR_L, \
    RENDER_ITEMS
from src.utils import texNode

if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'base.json'), 'r') as f:
        data = dict(merge(json.load(f), OVERLOAD_DATA))

    collector = LinesConstructor()
    for render_item in RENDER_ITEMS:  # type: str
        if RENDER_SEPARATOR_LR not in render_item:
            render_item += RENDER_SEPARATOR_LR
        _path, _choices = render_item.rsplit(RENDER_SEPARATOR_LR, 1)
        section = _path.rsplit(RENDER_SEPARATOR_L, 1)[-1]
        _data = data.copy()
        for _path in _path.split(RENDER_SEPARATOR_L):
            _data = _data[_path]
        if _choices:
            _data = [_data[key] for key in _choices.split(",")]
        if section in ['name', 'contactInfo']:
            item = texNode(section, *_data)
        elif section in ['summary']:
            item = SectionConstructor(SECTION_MAP[section])
            item.addDetail(_data)
        elif section in ['edu', 'work', 'private-projects']:
            item = SectionConstructor(SECTION_MAP[section])
            for line in _data:  # type: dict
                item.addPeriod(
                    line['org'],
                    line['title'],
                    line['period']
                )
                item.addDetail(line['detail'])
        else:
            raise ValueError(section)
        collector.add(item)
    collector.output(os.path.join(PROJECT_DIR, 'resume-hijiangtao/src/mark-base.tex'))
