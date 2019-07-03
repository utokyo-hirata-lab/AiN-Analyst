# AiN-Analyst

### Attom, iCap TQ, Nu Plasma 2 の統合解析ツールです。
- 2019年7月1日 NuPlasma2環境を実装 (溶液モード)
- 2019年7月1日 Attom環境を統合
- 2019年7月2日 Installation Tool (setup.py)を実装

## インストール
zipファイルをダウンロードし、以下のコマンドを実行してください。
```
python setup.py install
```
解析ファイルを作成し、hrtlab_coreをインポートしてください。
```
from hrtlab_core import *   #全てのツール
from hrtlab_core import nu2 #nu2モジュールのみ
from hrtlab_core import attom #Attomモジュールのみ
```

## Nu Plasma 2

csvファイルの読み込みは`data`関数で行います。Nu Plasma 2の場合は、`nu2`を呼び出して`data`関数を連結してください。
`nu2`呼び出し時にカップを指定してください。
```python
nu2 = nu2(['Cup1','Cup2','Cup3'])
nu2.data('読み込むcsvファイルの名前','データの名前','データタイプの指定')
```

`data`関数では、ブランクとサンプルでデータの読み込み方が異なります。ブランクの場合はデータタイプに`'b'`を指定、サンプルの場合は差し引くブランクを指定してください。
サンプルのデータ読み込み時に、指定したブランクの平均値が差し引かれます。
```python
nu2 = nu2(['H5','H2','L4']) #57Fe, 56Fe, 54Fe
nu2.data('Data_28089.csv','blank1','b') #ブランクData_28089.csvをblank1として読み込み
nu2.data('Data_28097.csv','blank2','b') #ブランクData_28097.csvをblank2として読み込み
nu2.data('Data_28090.csv','JMC1',['blank1','blank2']) #サンプルData_28090.csvをblank1とblank2の平均値を差し引いてJMC1として読み込み
```

読み込んだデータをもとに同位体比を計算することができます。`calc_isotopic_ratio`関数内で求めたい同位体比と対応するカップを指定してください。
```python
nu2.calc_isotopic_ratio('56Fe/54Fe','H2','L4')
nu2.calc_isotopic_ratio('57Fe/54Fe','H5','L4')
```

計算した同位体比をもとにδ値を計算できます。`calc_delta`関数で計算したい同位体比とスタンダード、サンプルを指定してください。
同位体比はリストで引き渡すことで複数のδ値を同時に計算できます。
```Python
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],'JMC1','Wako1')
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],'JMC2','Wako2')
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],'JMC3','Wako3')
```

読み込んだデータは、`check_data`関数で確認できます。
```python
nu2.check_data('blank1') #blank1の中身をチェック
nu2.check_data('57Fe/54Fe') #57Fe/54Feの計算結果をチェック
nu2.check_data('JMC1/Wako1') #JMC1/Wako1の計算されたδ値をチェック
```

読み込んだデータを`nu2`関数以外で使用したい場合は、`get_data`で取得できます。
```python
jmc_1 = nu2.get_data('JMC1','H2') #JMC1のH2のデータをjmc_1に代入
```

読み込んだデータをExcelフォーマットで出力することができます。`export`関数内で出力したいデータとファイル名を指定してください。オプションとして、読み込んだデータと同位体比の計算結果を全て出力することができます。その場合、変数名として`'all'`を指定してください。
```python
nu2.export('JMC1','JMC1.xlsx')  #JMC1の読み込んだデータを出力
nu2.export('56Fe/54Fe','56Fe_per_54Fe.xlsx')  #56Fe/54Feの計算結果を出力
nu2.export('all','result.xlsx') #全ての内容を出力
```

スリーアイソトーププロットは`three_isotope_vis`で作図できます。ラベルは自動生成されます。
```python
nu2.three_isotope_vis(xaxis_data,yaxis_data)
```
![Figure_1](https://user-images.githubusercontent.com/7247018/60564156-9bbe2e00-9d99-11e9-8755-e6c2541e5b74.png)


サンプルコード (main.py)
```python
from hrtlab_core import nu2

#データの読み込み
nu2 = nu2(['H5','H2','L4'])#57Fe, 56Fe, 54Fe
nu2.data('Data_28135.csv','blank1','b')
nu2.data('Data_28137.csv','blank2','b')
nu2.data('Data_28139.csv','blank3','b')
nu2.data('Data_28141.csv','blank4','b')
nu2.data('Data_28143.csv','blank5','b')
nu2.data('Data_28145.csv','blank6','b')
nu2.data('Data_28147.csv','blank7','b')
nu2.data('Data_28149.csv','blank8','b')
nu2.data('Data_28136.csv','JMC1',['blank1','blank2'])
nu2.data('Data_28138.csv','Wako1',['blank2','blank3'])
nu2.data('Data_28140.csv','JMC2',['blank3','blank4'])
nu2.data('Data_28142.csv','Wako2',['blank4','blank5'])
nu2.data('Data_28144.csv','JMC3',['blank5','blank6'])
nu2.data('Data_28146.csv','Wako3',['blank6','blank7'])
nu2.data('Data_28148.csv','JMC4',['blank7','blank8'])

#同位体比の計算
nu2.calc_isotopic_ratio('56Fe/54Fe','H2','L4')
nu2.calc_isotopic_ratio('57Fe/54Fe','H5','L4')

#データのチェックと取得と出力
nu2.check_data('JMC1')
nu2.check_data('56Fe/54Fe')
nu2.check_data('57Fe/54Fe')
nu2.export('JMC1','JMC1.xlsx')
nu2.export('56Fe/54Fe','isotopic_ratio.xlsx')
nu2.export('all','result.xlsx')
result1 = nu2.get_data('JMC1')
result2 = nu2.get_data('56Fe/54Fe')
print(result1)
```

Pythonでmain.pyを実行してください。
```Python
python main.py
```

## Attom

Attomの場合は、`attom`を呼び出して使用してください。
raw_dataディレクトリを作成し、予め全てのデータをこのディレクトリに格納しておいてください。
```python
attom = attom()
attom.binary2txt() #テキストファイルに変換します。
attom.txt2png() #テキストファイルをもとにpngファイルを作成します。
attom.txt2xlsx() #テキストファイルを全てエクセルファイルに統合します。
```
