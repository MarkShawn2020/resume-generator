## todo

- [ ] 【重要】对 tex 相对路径生成还不太了解，导致 instance and class 混杂在一起，需要深入研究改善，否则还不好使用 gitignore 控制

## usage

### pre-install

```shell
# to install tex: https://www.latex-project.org/get/
# for MacOS:
brew install --cask mactex

git clone --recursive https://github.com/MarkShawn2020/my-resume-generator && cd my-resume-generator
```

## json --> tex --> pdf

```shell
# 1. json --> tex
python main.py -f data/mark/base.json

# 2. tex --> pdf
#output to `out/base.pdf`
OUT=$PWD/out
mkdir -p $OUT && cd tex/hijiangtao/src && xelatex -output-directory=$OUT base.tex && cd -
```

## info

project of tex from `resume-hijiangtao`