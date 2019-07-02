# Analyst

### Nu Plasma 2, Attom, iCap TQの統合解析ツールです。
#### 2019年7月1日 NuPlasma2環境を実装
#### 2019年7月1日 Attom環境を統合

## 簡単な使用方法
解析ファイルを作成し、hrtlab_core.pyをインポートしてください。
```python
from hrtlab_core import *   #全てのツール
from hrtlab_core import nu2 #nu2モジュールのみ
```

## Nu Plasma 2

csvファイルの読み込みはdata関数で行います。Nu Plasma 2の場合は、nu2を呼び出してdata関数を連結してください。
nu2呼び出し時にカップを指定してください。
```python
nu2 = nu2(['Cup1','Cup2','Cup3'])
nu2.data('読み込むcsvファイルの名前','データの名前','データタイプの指定')
```

data関数では、ブランクとサンプルでデータの読み込み方が異なります。ブランクの場合はデータタイプに'b'を指定、サンプルの場合は差し引くブランクを指定してください。
サンプルのデータ読み込み時に、指定したブランクの平均値が差し引かれます。
```python
nu2 = nu2(['H5','H2','L4']) #57Fe, 56Fe, 54Fe
nu2.data('Data_28089.csv','blank1','b') #ブランクData_28089.csvをblank1として読み込み
nu2.data('Data_28097.csv','blank2','b') #ブランクData_28097.csvをblank2として読み込み
nu2.data('Data_28090.csv','JMC1',['blank1','blank2']) #サンプルData_28090.csvをblank1とblank2の平均値を差し引いてJMC1として読み込み
```

読み込んだデータをもとに同位体比を計算することができます。calc_isotopic_ratio関数内で求めたい同位体比と対応するカップを指定してください。
```python
nu2.calc_isotopic_ratio('56Fe/54Fe','H2','L4')
nu2.calc_isotopic_ratio('57Fe/54Fe','H5','L4')
```

読み込んだデータは、check_data関数で確認できます。
```python
nu2.check_data('blank1') #blank1の中身をチェック
```

読み込んだデータをnu2関数以外で使用したい場合は、get_dataで取得できます。
```python
jmc_1 = nu2.get_data('JMC1','H2') #JMC1のH2のデータをjmc_1に代入
```

読み込んだデータをExcelフォーマットで出力することができます。export関数内で出力したいデータとファイル名を指定してください。
```python
nu2.export('JMC1','JMC1.xlsx')
```

オプションとして、読み込んだデータと同位体比の計算結果を全て出力することができます。その場合、変数名として'all'を指定してください。
```python
nu2.export('all','result.xlsx')
```

サンプルコード
```python
from hrtlab_core import nu2

nu2 = nu2(['H5','H2','L4'])#57Fe, 56Fe, 54Fe
nu2.data('Data_28089.csv','blank1','b')
nu2.data('Data_28097.csv','blank2','b')
nu2.data('Data_28090.csv','JMC1',['blank1','blank2'])
nu2.data('Data_28091.csv','Wako1',['blank1','blank2'])
nu2.data('Data_28092.csv','JMC2',['blank1','blank2'])
nu2.data('Data_28093.csv','Wako2',['blank1','blank2'])
nu2.data('Data_28094.csv','JMC3',['blank1','blank2'])
nu2.data('Data_28095.csv','Wako3',['blank1','blank2'])
nu2.data('Data_28096.csv','JMC4',['blank1','blank2'])
#nu2.check_data('JMC4')
#a = nu2.get_data('JMC4','H2')

#nu2.box_vis(['JMC1','JMC2','JMC3','JMC4'],'H2') #56Fe
#nu2.scatter_vis(calc_delta(JMC1,Wako1),'Cycle',"$\delta^{56}Fe(‰)$")
```

## Attom

Attomの場合は、attomを呼び出して使用してください。
raw_dataディレクトリを作成し、予め全てのデータをこのディレクトリに格納しておいてください。
```python
attom = attom() 
attom.binary2txt() #テキストファイルに変換します。
attom.txt2png() #テキストファイルをもとにpngファイルを作成します。
attom.txt2xlsx() #テキストファイルを全てエクセルファイルに統合します。
```
