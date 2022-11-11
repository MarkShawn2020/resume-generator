
## info

project of tex from `resume-hijiangtao`

## usage

### pre-install

```shell
# for running `pdflatex` in webstorm
brew install --cask mactex
```


## 1. json --> tex

output to `TeX/src/base.pdf`

```shell
python main.py -f data/mark/base.json
```

## 2. tex --> pdf

output to `out/base.pdf`
```shell
mkdir -p out && cd TeX/src && xelatex -output-directory=../../out base.tex && cd -
```