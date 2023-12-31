# pickle-encoder
pickle encoder for image classification

### pickle encoderはラベルと画像データのペアとしてpickle形式で指定のディレクトリに保存してくれるモジュールである。

用途としては、一からデータセットを作り、dlで画像分類などをするときに役立つ。

ディレクトリ構造
```bash
.
├── LICENSE
├── README.md
├── data
│   ├── 01_1yen
│   ├── 02_5yen
│   ├── 03_10yen
│   ├── 04_50yen
│   ├── 05_100yen
│   └── 06_500yen
├── encoding.py
├── pickle_encoder.py
└── picklevenv
    ├── bin
    ├── include
    ├── lib
    ├── pyvenv.cfg
    └── share
```
## 使い方

ターミナルで当該リポジトリをクローンし、リポジトリ内に存在する仮想環境を有効にする
```bash
git clone https://github.com/koki-takada-1/pickle-encoder.git
. picklevenv/bin/activate
```
opencvをインストール
```
pip install opencv-python
```

モジュールを以下のようにインポートして使う。
```python
from pickle_encoder import PickleEncoding
# 画像の枚数指定
maxsize = 600
out_dir = "data"
# pickleファイルの名前指定
save_file = "/name.pickle"
# 正方形の辺のサイズ指定
size = 200

pe = PickleEncoding(maxsize, out_dir, save_file)
pe.resize_encoding(size)
```
