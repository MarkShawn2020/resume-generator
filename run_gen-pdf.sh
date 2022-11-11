FILE_NAME=base

# 1. json --> tex
python gen_tex.py -f data/mark/$FILE_NAME.json

# 2. tex --> pdf
OUT=$PWD/out # output to `out/base.pdf`
mkdir -p $OUT && cd tex/hijiangtao/src && xelatex -output-directory=$OUT $FILE_NAME && cd -

open $OUT/$FILE_NAME.pdf