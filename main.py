from hrtlab_core import nu2

#データの読み込み
nu2 = nu2(['H5','H2','L4'])#57Fe, 56Fe, 54Fe
nu2.data('Data_28213.csv','blank1','b')
nu2.data('Data_28215.csv','blank2','b')
nu2.data('Data_28217.csv','blank3','b')
nu2.data('Data_28219.csv','blank4','b')
nu2.data('Data_28221.csv','blank5','b')
nu2.data('Data_28223.csv','blank6','b')
nu2.data('Data_28225.csv','blank7','b')
nu2.data('Data_28227.csv','blank8','b')
nu2.data('Data_28214.csv','JMC1',['blank1','blank2'])
nu2.data('Data_28216.csv','Wako1',['blank2','blank3'])
nu2.data('Data_28218.csv','JMC2',['blank3','blank4'])
nu2.data('Data_28220.csv','Wako2',['blank4','blank5'])
nu2.data('Data_28222.csv','JMC3',['blank5','blank6'])
nu2.data('Data_28224.csv','Wako3',['blank6','blank7'])
nu2.data('Data_28226.csv','JMC4',['blank7','blank8'])

#同位体比の計算
nu2.calc_isotopic_ratio('56Fe/54Fe','H2','L4')
nu2.calc_isotopic_ratio('57Fe/54Fe','H5','L4')

#δ値の計算
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],['JMC1','JMC2'],'Wako1')
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],['JMC2','JMC3'],'Wako2')
nu2.calc_delta(['56Fe/54Fe','57Fe/54Fe'],['JMC3','JMC4'],'Wako3')

#データのチェックと取得と出力
#nu2.check_data('JMC1/Wako1')
#nu2.check_data('JMC2/Wako2')
#nu2.check_data('JMC3/Wako3')
#nu2.export('JMC2/Wako2','JMC2perWako2.xlsx')
#nu2.check_data('JMC1')
#nu2.check_data('56Fe/54Fe')
#nu2.check_data('57Fe/54Fe')
#nu2.export('JMC1','JMC1.xlsx')
#nu2.export('56Fe/54Fe','isotopic_ratio.xlsx')
nu2.export('all','result.xlsx')
#result1 = nu2.get_data('JMC1')
#result2 = nu2.get_data('56Fe/54Fe')
#result3 = nu2.get_data('JMC1/Wako1')
#print(result1)

#作図
nu2.box_vis('H2',['blank1','blank2','blank3','blank4','blank5','blank6','blank7','blank8'])
nu2.box_vis('H2',['JMC1','JMC2','JMC3','JMC4']) #56Fe
nu2.box_vis('57Fe/54Fe',['JMC1','JMC2','JMC3','JMC4']) #56Fe
nu2.box_vis('H2',['Wako1','Wako2','Wako3']) #56Fe
nu2.box_vis('H2',['JMC1','Wako1','JMC2','Wako2','JMC3','Wako3','JMC4']) #56Fe
nu2.box_vis('H2',['blank1','JMC1','blank2','Wako1','blank3','JMC2','blank4','Wako2','blank5','JMC3','blank6','Wako3','blank7','JMC4','blank8'])
#nu2.scatter_vis(calc_delta(JMC1,Wako1),'Cycle',"$\delta^{56}Fe(‰)$")
nu2.three_isotope_vis('56Fe/54Fe','57Fe/54Fe') #x,y
