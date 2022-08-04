# 概要
[ずんだもんのROHAN_4600音声データセット](https://zunko.jp/multimodal_dev/login.php)に関する音素とアクセントのラベルです。音素アライメントラベルは含んでおりません。

PyOpenjtalkの出力を人手で修正しました。
修正は周波数メルスペクトログラム（対数メモリ）を見ながら音声を聴いて修正しています。

当方は素人ですので精度に関しては保証しかねますが、PyOpenjtalkの出力をそのまま用いるよりは良いかと思います。

使用・修正はご自由に行ってください。修正版の再配布に関しましても問題ありません。

ただし、本ラベルの使用に関するあらゆる不利益に対しては責任を負いかねますので、自己責任の上での使用をお願いいたします。

# 内容説明
### /phoneme_data
音声ファイルごとの音素のラベルデータ
### /accente_data
音声ファイルごとのアクセントのラベルデータ
### /vvproj_data
vvprojファイルが入っております。[VOICE VOX](https://voicevox.hiroshiba.jp/)を用いて音素やアクセントを調整することができます。修正時にお役立てください。

### /csv_data
音素及びアクセントに関するデータがcsv形式で含まれています。

### vvp_to_csv.py
vvprojファイルからphoneme_and_accent.csvを作成します。

### csv_extract.py
phoneme_and_accent.csvからphoneme.csvとaccent.csvを作成します。

### csv_processor.py
phoneme.csvとaccent.csvから/phoneme_dataと/accent_dataを作成します。

# ラベル形式
### phoneme_list & accent_list

```
phoneme_list = ['pau', 'I', 'N', 'U', 'a', 'b', 'by', 'ch', 'cl', 'd', 'dy', 'e', 'f', 'g', 'gy', 'h', 'hy', 'i', 'j', 'k', 'ky', 'm', 'my', 'n', 'ny', 'o', 'p', 'py', 'r', 'ry', 's', 'sh', 't', 'ts', 'ty', 'u', 'v', 'w', 'y', 'z']
accent_list = ['_', '[', ']', '#', '?']
```

### アクセント記号

```
_ : 情報なし
[ : ピッチ上がり
] : ピッチ下がり（アクセント核）
# : アクセント境界
? : アクセント境界（疑問文・末尾のみ）
```

### 音素・アクセント表記例

```
ROHAN4600_0002:ゲグァンはこのところ他者を見下すし、ちょっと脅かすか？

[ROHAN4600_0002.ph]
g e g u a N w a k o n o t o k o r o t a sh a o m i k u d a s u sh i pau ch o cl t o o d o k a s u k a

[ROHAN4600_0002.ac]
_ ] _ _ _ _ _ # _ [ _ _ _ _ _ _ _ # _ ] _ _ # _ [ _ _ _ _ _ ] _ _ # _ ] _ _ # [ _ _ _ ] _ _ _ ?
```
# クレジット
## ラベリング担当
0001~3950：とろわーる

3951~4600：seichi様

## コード提供
Yちゃん様

# リンク
## ROHAN4600：モーラバランス型日本語コーパス
https://github.com/mmorise/rohan4600

## ROHAN4600マルチモーダルデータベース
https://zunko.jp/multimodal_dev/login.php

# ご連絡
なにかありましたら[Twitter](https://twitter.com/RRR_troisR_888)の方までお願いいたします。