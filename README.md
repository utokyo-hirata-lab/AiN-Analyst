# Analyst

### Nu Plasma 2, Attom, iCap TQの統合解析ツールです。
2019年7月1日 NuPlasma2環境を実装

## 簡単な使用方法
解析ファイルを作成し、hrtlab_core.pyをインポートしてください。
```python
from hrtlab_core import *
```
csvファイルの読み込みはdata関数で行います。Nu Plasma 2の場合は、nu2を呼び出してdata関数を連結してください。
nu2呼び出し時にカップを指定してください。
data関数では、ブランクとサンプルでデータの読み込み方が異なります。ブランクの場合はid = 'b'、サンプルの場合は差し引くブランクを指定してください。
サンプルのデータ読み込み時に、指定したブランクの平均値が差し引かれます。
```python
nu2 = nu2(['H5','H2','L4']) #57Fe, 56Fe, 54Fe
nu2.data('Data_28089.csv','blank1','b')
nu2.data('Data_28089.csv','blank1','b')
nu2.data('Data_28097.csv','blank2','b')
nu2.data('Data_28090.csv','JMC1',['blank1','blank2'])
```

## Nu Plasma 2
```python
from hrtlab_core import *

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
#nu2.dot_vis(calc_delta(JMC1,Wako1),'Cycle',"$\delta^{56}Fe(‰)$")
```
