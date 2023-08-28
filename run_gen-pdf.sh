NAME=cv
python main_gen_tex.py -f config/${NAME}.json

( OUT=$PWD/out && mkdir -p $OUT && cd tex/hijiangtao/src && xelatex -output-directory=$OUT ${NAME}.tex )
