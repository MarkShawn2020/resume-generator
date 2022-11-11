## info

project of tex from `resume-hijiangtao`

## usage

### pre-install

```shell
# for running `pdflatex` in webstorm
brew install --cask mactex
```

## json --> tex --> pdf

```shell
# 1. json --> tex
python main.py -f data/mark/base.json

# 2. tex --> pdf
#output to `out/base.pdf`
OUT=$PWD/out
mkdir -p $OUT && cd tex/src/hijiangtao && xelatex -output-directory=$OUT base.tex && cd -
```
