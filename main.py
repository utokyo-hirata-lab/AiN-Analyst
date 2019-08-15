from hrtlab_core import nu2

#データの読み込み
nu2 = nu2(['H7','H3','L1'],['44Ca','43Ca','42Ca'])
nu2.data('Data_28480.csv','blank1','b')
nu2.data('Data_28488.csv','blank2','b')
nu2.data('Data_28481.csv','STD1',['blank1','blank2'])
nu2.data('Data_28482.csv','SAMPLE1',['blank1','blank2'])
nu2.data('Data_28483.csv','STD2',['blank1','blank2'])
nu2.data('Data_28484.csv','SAMPLE2',['blank1','blank2'])
nu2.data('Data_28485.csv','STD3',['blank1','blank2'])
nu2.data('Data_28486.csv','SAMPLE3',['blank1','blank2'])
nu2.data('Data_28487.csv','STD4',['blank1','blank2'])

#同位体比の計算
nu2.calc_isotopic_ratio('44Ca/42Ca')
nu2.calc_isotopic_ratio('43Ca/42Ca')

#δ値の計算
nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD1','STD2'],'SAMPLE1')
nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD2','STD3'],'SAMPLE2')
nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD3','STD4'],'SAMPLE3')

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
nu2.cycle_vis('42Ca',['blank1','blank2'])
nu2.cycle_vis('42Ca',['STD1','STD2','STD3','STD4'])
nu2.cycle_vis('43Ca',['STD1','STD2','STD3','STD4'])
nu2.cycle_vis('44Ca',['STD1','STD2','STD3','STD4'])
nu2.box_vis('42Ca',['STD1','STD2','STD3','STD4'])
nu2.box_vis('43Ca',['STD1','STD2','STD3','STD4'])
nu2.box_vis('44Ca',['STD1','STD2','STD3','STD4'])
nu2.cycle_vis('44Ca/42Ca',['STD1','STD2','STD3','STD4'])
nu2.cycle_vis('43Ca/42Ca',['STD1','STD2','STD3','STD4'])
nu2.box_vis('44Ca/42Ca',['STD1','STD2','STD3','STD4'])
nu2.box_vis('43Ca/42Ca',['STD1','STD2','STD3','STD4'])
"""
nu2.box_vis('57Fe/54Fe',['JMC1','JMC2','JMC3','JMC4']) #56Fe
nu2.box_vis('H2',['Wako1','Wako2','Wako3']) #56Fe
nu2.box_vis('H2',['JMC1','Wako1','JMC2','Wako2','JMC3','Wako3','JMC4']) #56Fe
nu2.box_vis('H2',['blank1','JMC1','blank2','Wako1','blank3','JMC2','blank4','Wako2','blank5','JMC3','blank6','Wako3','blank7','JMC4','blank8'])
#nu2.scatter_vis(calc_delta(JMC1,Wako1),'Cycle',"$\delta^{56}Fe(‰)$")
"""
nu2.three_isotope_vis('43Ca/42Ca','44Ca/42Ca') #x,y
