# PyScanMate

## How to use

### 1, 仮想環境準備（必要なら）

適当なディレクトリを作成して、ターミナルを開く

・仮想環境準備

`python -m venv venv`

・仮想環境起動

`. venv/bin/activate`

---

### 2, install package

・インストール

`pip install git+https://github.com/akilasatolu/PyScanMate.git`

・インストール確認

`pip list`

---

### 3, 使ってみよう

適当な`.py`ファイルを作成して、packageをimportして使ってみよう

`import pyscanmate`

`pyscanmate.モジュール名()`

---

### 4, お片付け

・アンインストール

`pip uninstall pyscanmate`

・仮想環境終了

`deactivate`

・アンインストール確認

`pip list`

---

### 5, その他

・アップグレード

`pip install –upgrade pyscanmate`

## 関数一覧

============================

### `get_files(path, reg, hidden)`

指定したディレクトリ配下のファイル名を全取得する。

戻り値は、`[]` `[str, str, ...]`

ファイル名を格納したリスト、もしくはファイルがなければ空のリストを返す。

---

`path`

指定したいディレクトリの相対パスを記載する。

例 : `'test'` `'test/src'`

---

`reg`（省略可）

デフォルト値 : `r'.*$'`

文字列または正規表現で拡張子もしくはファイル名を指定する。
デフォルトは全ての拡張子を指定。
正規表現使用時は先頭にrを付与する。

例 : `r'.*$'` `r'.js$'` `'aaa'`

---

`hidden`（省略可）

デフォルト値 : `False`

隠しファイルを含むかどうかを指定する。
デフォルトは隠しファイルを含まない。

例 : `True` `False`

============================

### `format_txt(str_list, before_reg, after)`

リストの文字列を置換する。

戻り値は、`[]` `[str, str, ...]`

`str_list`が空の場合はそのまま返す。
置換後のリストを返す。

---

`str_list`

文字列の入った配列。

例 : `[]` `['aaa', 'bbb']`

---

`before_reg`

置換対象。文字列または正規表現。

例 : `'test'` `r'.(js|css)$'`

バックスラッシュは`r\\`。

---

`after`（省略可）

置換後の文字列。
デフォルトは`''`で対象を除去する。

例 : `''` `'str'`

============================

### `grep(path, keywords)`

指定のディレクトリ配下でキーワードでGrepを行う。

戻り値は、`[{'keyword': str, 'is_used': bool, 'where': []}, {'keyword': str, 'is_used': bool, 'where': [{'file': str, 'line': [int, int, ...]}, ...]}, ...]`

`keyword`は検索するキーワード、`is_used`は使用されていれは`True`なければ`False`を返す。
`where`には使用しているファイル情報が記載されている。
`file`はファイル名、`line`は行番号がリストに格納されている。

---

`path`

指定したいディレクトリの相対パスを記載する。

例 : `test/src`

---

`keywords`

検索するキーワードのリスト。

例 : `['.js','txt']` `['import', export]`

============================

### `count_line(path, trim_blank)`

指定のディレクトリ配下にある全ファイルのコード量をカウントする。

戻り値は、`0` `12` `int`

---

`path`

指定したいディレクトリの相対パスを記載する。

例 : `test/src`

---

`trim_blank`（省略可）

空行を無視するかどうか。
デフォルトは`False`で無視しない。
`True`で無視する。

例 : `True` `False`

============================