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
#nu2.check_data('JMC1')
#nu2.check_data('56Fe/54Fe')
#nu2.check_data('57Fe/54Fe')
#nu2.export('JMC1','JMC1.xlsx')
#nu2.export('56Fe/54Fe','isotopic_ratio.xlsx')
#nu2.export('all','result.xlsx')
#result1 = nu2.get_data('JMC1')
#result2 = nu2.get_data('56Fe/54Fe')
#print(result1)

#作図
#nu2.box_vis('H2',['blank1','blank2','blank3','blank4','blank5','blank6','blank7','blank8'])
#nu2.box_vis('H2',['JMC1','JMC2','JMC3','JMC4']) #56Fe
nu2.box_vis('57Fe/54Fe',['JMC1','JMC2','JMC3','JMC4']) #56Fe
#nu2.box_vis('H2',['Wako1','Wako2','Wako3']) #56Fe
#nu2.box_vis('H2',['JMC1','Wako1','JMC2','Wako2','JMC3','Wako3','JMC4']) #56Fe
#nu2.box_vis('H2',['blank1','JMC1','blank2','Wako1','blank3','JMC2','blank4','Wako2','blank5','JMC3','blank6','Wako3','blank7','JMC4','blank8'])
#nu2.scatter_vis(calc_delta(JMC1,Wako1),'Cycle',"$\delta^{56}Fe(‰)$")
