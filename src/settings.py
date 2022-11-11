"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 10, 2022, 19:38
"""
import os

SRC_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
TEX_SRC_DIR = os.path.join(PROJECT_DIR, 'tex/hijiangtao/src')

PAGE_NUMBERING_VISIBILITY = False
LANG_ZH = 'zh'
LANG_EN = 'en'
LANG = LANG_ZH
COMMA = '，' if LANG == LANG_ZH else ', '

PART_SPECIAL = ['name', 'contactInfo']
PART_SIMPLE_SECTIONS = ['summary']
PART_PERIOD_SECTIONS = ['edu', 'work', 'private-projects']

SECTION_NAME_MAP = {
    "edu"             : "教育经历",
    "work"            : "工作经历",
    "open-source"     : "开源项目",
    "private-projects": "个人项目",
    "headline"        : "我是",
    "summary"         : "个人总结"
}

RENDER_SEPARATOR_LR = ':'
RENDER_SEPARATOR_L = "."
RENDER_SEPARATOR_R = ","

RENDER_ITEMS = [
    "basis.name:zh-nickname",
    "basis.contactInfo:email-foreign,mobile,MBTI,target",
    "summary",
    "experience.work:arpara,anyong,huaxing",
    "experience.edu:NAU,CUHKSZ,UESTC",
    # "experience.private-projects:docusaurus",
]

OVERLOAD_DATA = {
    "basis": {
        "contactInfo": {
            "target": "期望岗位：研发"
        }
    }
}
