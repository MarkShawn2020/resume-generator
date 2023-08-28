"""
source: own
author: https://github.com/MarkShawn2020
create: Nov 11, 2022, 13:23
"""
import argparse
import os

from src.core import generateResumeTex
from src.lib.path import PROJECT_DIR

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', help='JSON格式基本资料文件地址')
    args = parser.parse_args()

    generateResumeTex(
        os.path.join(PROJECT_DIR, args.file_path or 'data/mark/base.json'),
    )
