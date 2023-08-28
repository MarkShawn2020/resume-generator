NAME=base
python main_gen_tex.py -f data/mark/${NAME}.json

OUT=$PWD/out
mkdir -p $OUT && cd tex/hijiangtao/src && xelatex -output-directory=$OUT ${NAME}.tex && cd -
