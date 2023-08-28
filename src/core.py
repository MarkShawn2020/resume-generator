"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 18:40
"""
import json
import os.path

from mergedeep import merge

from src.LinesConstructor import LinesConstructor
from src.SectionConstructor import SectionConstructor
from src.settings import RENDER_SEPARATOR_LR, \
    RENDER_SEPARATOR_L
from src.lib.path import PROJECT_DIR, TEX_SRC_DIR
from src.utils import texNode

with open(PROJECT_DIR / "config/ui.json") as f:
    ui_config = json.load(f)
    section_name_map = ui_config["section_name_map"]
    overload_data = ui_config["overload"]
    render_items = ui_config["render_items"]
    parts = ui_config["parts"]
    PART_SPECIAL = parts["special"]
    PART_SIMPLE_SECTIONS = parts["simple"]
    PART_PERIOD_SECTIONS = parts["period"]


def generateResumeTex(fp: str):
    with open(fp, 'r') as f:
        data = dict(merge(json.load(f), overload_data))
    
    collector = LinesConstructor()
    for render_item in render_items:  # type: str
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
            item = SectionConstructor(section_name_map[part])
            item.addDetail(_data)
        elif part in PART_PERIOD_SECTIONS:
            item = SectionConstructor(section_name_map[part])
            for line in _data:  # type: dict
                item.addPeriod(line)
                item.addDetail(line)
        else:
            raise ValueError(part)
        collector.add(item)
    
    fn = os.path.basename(fp).rsplit('.', 1)[0]
    collector.output(os.path.join(TEX_SRC_DIR, f'{fn}.tex'))
