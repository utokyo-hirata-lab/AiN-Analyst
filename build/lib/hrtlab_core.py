#August 15, 2019
import csv
import os
import sys
import re
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_pdf import PdfPages
from statistics import mean, median,variance,stdev
import tkinter as tk
import tkinter.messagebox, tkinter.filedialog
import glob

class pycolor:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

class element:
    def __init__(self):
        self.DataBase = {}
        self.DataBase.update({'42Ca':41.95862})
        self.DataBase.update({'43Ca':42.95877})
        self.DataBase.update({'44Ca':43.95548})
        self.DataBase.update({'54Fe':53.93961})
        self.DataBase.update({'56Fe':55.93494})
        self.DataBase.update({'57Fe':56.93539})
        self.DataBase.update({'58Fe':57.93327})
        self.DataBase.update({'63Cu':62.92960})
        self.DataBase.update({'64Zn':63.92914})
        self.DataBase.update({'65Cu':64.92779})
        self.DataBase.update({'66Zn':65.92603})
        self.DataBase.update({'67Zn':66.92713})
        self.DataBase.update({'68Zn':67.92484})

    def add(self,el,mass):
        self.DataBase.update({el:mass})

    def info(self,el):
        return self.DataBase[el]

    def list(self):
        for el in self.DataBase.keys():
            print(el,':',self.DataBase[el])

def vis_params():
    #plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 18
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.major.width'] = 1.0
    plt.rcParams['ytick.major.width'] = 1.0
    plt.rcParams['lines.linewidth'] = 0.8

try: from sklearn import linear_model;clf = linear_model.LinearRegression()
except ModuleNotFoundError:
    print('sklearn module was not found.')
    print('You should run '+pycolor.RED +'\"pip install sklearn\"'+pycolor.END)
    sys.exit()

try: import xlrd
except ModuleNotFoundError:
    print('xlrd module was not found.')
    print('You should run '+pycolor.RED +'\"pip install xlrd\"'+pycolor.END)
    sys.exit()

try: import openpyxl
except ModuleNotFoundError:
    print('openpyxl module was not found.')
    print('You should run '+pycolor.RED +'\"pip install openpyxl\"'+pycolor.END)
    sys.exit()

try: import xlwt
except ModuleNotFoundError:
    print('xlwt module was not found.')
    print('You should run '+pycolor.RED +'\"pip install xlwt\"'+pycolor.END)
    sys.exit()

try: import xlsxwriter
except ModuleNotFoundError:
    print('xlsxwriter module was not found.')
    print('You should run '+pycolor.RED +'\"pip install xlsxwriter\"'+pycolor.END)
    sys.exit()

try: import pprint
except ModuleNotFoundError:
    print('pprint module was not found.')
    print('You should run '+pycolor.RED +'\"pip install pprint\"'+pycolor.END)
    sys.exit()

try: import glob
except ModuleNotFoundError:
    print('glob module was not found.')
    print('You should run '+pycolor.RED +'\"pip install glob\"'+pycolor.END)
    sys.exit()

try: import pandas
except ModuleNotFoundError:
    print('pandas module was not found.')
    print('You should run '+pycolor.RED +'\"pip install pandas\"'+pycolor.END)
    sys.exit()

try: import seaborn as sns
except ModuleNotFoundError:
    print('seaborn module was not found.')
    print('You should run '+pycolor.RED +'\"pip install seaborn\"'+pycolor.END)
    sys.exit()

class template:
    def __init__(self):
        pass

    def nu2(self,result):
        with open(result, 'w') as f:
            f.write("from hrtlab_core import nu2\n")
            f.write("#データの読み込み\n")
            f.write("nu2 = nu2(['H7','H3','L1'],['44Ca','43Ca','42Ca'])\n")
            f.write("#nu2.data('Data_28480.csv','blank1','b')\n")
            f.write("#nu2.data('Data_28488.csv','blank2','b')\n")
            f.write("#nu2.data('Data_28481.csv','STD1',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28482.csv','SAMPLE1',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28483.csv','STD2',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28484.csv','SAMPLE2',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28485.csv','STD3',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28486.csv','SAMPLE3',['blank1','blank2'])\n")
            f.write("#nu2.data('Data_28487.csv','STD4',['blank1','blank2'])\n")
            for file in sorted(glob.glob('*.csv')):f.write("nu2.data('"+file+"','','')\n")
            f.write("#同位体比の計算\n")
            f.write("nu2.calc_isotopic_ratio('44Ca/42Ca')\n")
            f.write("nu2.calc_isotopic_ratio('43Ca/42Ca')\n")
            f.write("#δ値の計算\n")
            f.write("nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD1','STD2'],'SAMPLE1')\n")
            f.write("nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD2','STD3'],'SAMPLE2')\n")
            f.write("nu2.calc_delta(['43Ca/42Ca','44Ca/42Ca'],['STD3','STD4'],'SAMPLE3')\n")
            f.write("#データのチェックと取得と出力\n")
            f.write("nu2.export('all','result.xlsx')\n")
            f.write("#作図\n")
            f.write("nu2.cycle_vis('42Ca',['blank1','blank2'])\n")
            f.write("nu2.cycle_vis('42Ca',['STD1','STD2','STD3','STD4'])\n")
            f.write("nu2.cycle_vis('43Ca',['STD1','STD2','STD3','STD4'])\n")
            f.write("nu2.cycle_vis('44Ca',['STD1','STD2','STD3','STD4'])\n")
            f.write("nu2.cycle_vis('44Ca/42Ca',['STD1','STD2','STD3','STD4'])\n")
            f.write("nu2.cycle_vis('43Ca/42Ca',['STD1','STD2','STD3','STD4'])\n")
            f.write("nu2.three_isotope_vis('43Ca/42Ca','44Ca/42Ca')\n")

class nu2:
    def __init__(self,cup,cl):
        self.element = element()
        self.cup = cup
        self.cup_element = cl
        self.dataset = {}
        self.ir_list = {}
        #self.ir = pd.DataFrame({})
        self.ir_length = 0
        self.delta_list = {}
        self.delta_SE_list = {}
        #self.delta = pd.DataFrame({})

    def data(self,data,name,id):
        if id == 'b':
            self.dataset[name] = self.read_blank(data)
            if self.ir_length < len(self.dataset[name][0]):self.ir_length = len(self.dataset[name][0])
        else:
            blank_list = [self.dataset[i] for i in id]
            blank = [sum(e)/len(e) for e in zip(*blank_list)]
            self.dataset[name] = self.read_sample(data,blank)
            if self.ir_length < len(self.dataset[name][0]):self.ir_length = len(self.dataset[name][0])

    def check_params(self):
        print('Cup : ',self.cup)

    def check_data(self,name):
        if name in self.dataset:
            result = pd.DataFrame({})
            for cup_name in self.cup:
                result[cup_name] = self.dataset[name][self.cup.index(cup_name)]
            print('\n'+name+'\n')
            print(result)
        elif name in self.ir_list:
            print('\n'+name+'\n')
            print(self.ir_list[name])
        elif name in self.delta_list:
            print('\n'+name+'\n')
            print(self.delta_list[name])
        else:
            print('\n'+name+' : Not found !')

    def get_data(self,name):
        if name in self.dataset:
            result = pd.DataFrame({})
            for cup_name in self.cup_element:
                result[cup_name] = self.dataset[name][self.cup_element.index(cup_name)]
            return result
        elif name in self.ir_list:
            return self.ir_list[name]
        elif name in self.delta_list:
            return self.delta_list[name]
        else:
            print('\n'+name+' : Not found !')

    def export(self,data,filename):
        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            if data == 'all':
                for i in self.dataset.keys():
                    result = pd.DataFrame({})
                    for cup_name in self.cup_element:
                        result[cup_name] = self.dataset[i][self.cup_element.index(cup_name)]
                    result.to_excel(writer,sheet_name=i)
                    self.exformat(writer,result,i)
                for i in self.ir_list.keys():
                    self.ir_list[i].to_excel(writer,sheet_name=i.replace('/','per'))
                    self.exformat(writer,self.ir_list[i],i.replace('/','per'))
                output = pd.DataFrame({})
                for i in self.delta_list.keys():
                    result = pd.DataFrame({})
                    for j in list(self.delta_list[i].keys()):
                        result[i.split('/')[1]] = pd.Series(self.delta_list[i])
                        result[i.split('/')[1]+'_SE'] = pd.Series(self.delta_SE_list[i])
                    output = pd.concat([output,result],axis=1)
                output.to_excel(writer,sheet_name='delta')
                self.exformat(writer,output,'delta')
            elif data in self.dataset:
                result = pd.DataFrame({})
                for cup_name in self.cup_element:
                    result[cup_name] = self.dataset[data][self.cup_element.index(cup_name)]
                result.to_excel(writer, sheet_name=data)
                self.exformat(writer,result,data.replace('/','per'))
            elif data in self.ir_list:
                self.ir_list[data].to_excel(writer,sheet_name=data.replace('/','per'))
                self.exformat(writer,self.ir_list[data],data.replace('/','per'))
            elif data in self.delta_list:
                result = pd.DataFrame({})
                for i in list(self.delta_list[data].keys()):
                    result[data] = pd.concat([pd.Series(self.delta_list[data]),pd.Series(self.delta_SE_list[data])])
                result.to_excel(writer,sheet_name=data.replace('/','per'))
                self.exformat(writer,result,data.replace('/','per'))
            else:
                print('\n'+data+' : Not found !')

    def exformat(self,writer,data,sheetname):
        workbook,worksheet = writer.book,writer.sheets[sheetname]
        fmt = workbook.add_format({'bold': False,"border": 0})
        [worksheet.write(0, col_num, col_value, fmt) for col_num, col_value in enumerate(data.columns.values, 1)]
        [worksheet.write(idx_num, 0, idx_value, fmt) for idx_num, idx_value in enumerate(data.index.values, 1)]

    def read_blank(self,filename):
        file,j = open(filename).readlines(),0
        for line in file:
            if line.split(',')[0] == 'Cycle':index = j
            j += 1
        data,col,ind,result = file[index+1::],[],[i.rstrip() for i in file[index].split(',')],[]; del ind[-1];
        for line in range(len(data)):
            col.append(int(data[line].rstrip().split(',')[0]))
            data[line] = data[line].rstrip().split(',')[1::]
            data[line] = [float(i) for i in data[line]]
        ind = [i.replace(' (','').replace(')','') for i in ind]
        df = pd.DataFrame(data,index=col,columns=ind[1::])
        for cupid in range(len(self.cup)):result.append(df[self.cup[cupid]+str(1)] - df[self.cup[cupid]+str('Z1')])
        return result

    def read_sample(self,filename,blank):
        file,j = open(filename).readlines(),0
        for line in file:
            if line.split(',')[0] == 'Cycle':index = j
            j += 1
        data,col,ind,result = file[index+1::],[],[i.rstrip() for i in file[index].split(',')],[]; del ind[-1];
        for line in range(len(data)):
            col.append(int(data[line].rstrip().split(',')[0]))
            data[line] = data[line].rstrip().split(',')[1::]
            data[line] = [float(i) for i in data[line]]
        ind = [i.replace(' (','').replace(')','') for i in ind]
        df = pd.DataFrame(data,index=col,columns=ind[1::])
        for cupid in range(len(self.cup)):result.append(df[self.cup[cupid]+str(1)] - df[self.cup[cupid]+str('Z1')] - blank[cupid].mean())
        return result

    def calc_isotopic_ratio(self,ratio):
        vsh = self.cup[self.cup_element.index(ratio.split('/')[0])]
        vsl = self.cup[self.cup_element.index(ratio.split('/')[1])]
        ir = pd.DataFrame(np.zeros([self.ir_length,len(self.dataset.keys())]),index=range(1,self.ir_length+1),columns=self.dataset.keys())
        for name in self.dataset.keys():
            high = self.dataset[name][self.cup.index(vsh)]
            low = self.dataset[name][self.cup.index(vsl)]
            ir[name] = high/low
        self.ir_list[ratio] = ir

    def calc_delta(self,ratio_list,standard,sample):
        std1 = standard[0]
        std2 = standard[1]
        delta,delta_SE = {},{}
        for ratio in ratio_list:
            std1_SE   = np.std(self.ir_list[ratio][std1],ddof=1)/np.sqrt(len(self.ir_list[ratio][std1]))
            std2_SE   = np.std(self.ir_list[ratio][std2],ddof=1)/np.sqrt(len(self.ir_list[ratio][std2]))
            sample_SE = np.std(self.ir_list[ratio][sample],ddof=1)/np.sqrt(len(self.ir_list[ratio][sample]))
            std_SE    = np.sqrt(std1_SE**2+std2_SE**2)/2
            std       = (self.ir_list[ratio][std1]+self.ir_list[ratio][std2])/2
            smp       = self.ir_list[ratio][sample]
            quotient  = smp.mean()/std.mean()
            delta.update({ratio:((quotient-1)*1000)})
            delta_SE.update({ratio:np.sqrt((sample_SE/std.mean())**2+(quotient*std_SE/std.mean())**2)*1000})
        self.delta_list[str('mean('+std1+std2+')/'+sample)] = delta
        self.delta_SE_list[str('mean('+std1+std2+')/'+sample)] = delta_SE

    def cycle_vis(self,el,name):
        Tintegr = 5 #integration time (s)
        vis_params()
        dataf = pd.DataFrame({})
        graygrid = []
        dataf = pd.DataFrame({})
        fig = plt.figure(figsize=(10,7))
        axl = fig.add_subplot(1, 1, 1)
        axr = axl.twinx()
        if el in self.cup_element:
            for i in range(len(name)):
                dataf = pd.concat([dataf,self.dataset[name[i]][self.cup_element.index(el)]])
                graygrid.append(len(dataf))
                axl.set_ylabel('Intensity of '+self.vis_label(el)+' / V')
                axr.set_ylabel('Deviation (%)')
        elif el in self.ir_list:
            for i in range(len(name)):
                dataf = pd.concat([dataf,self.ir_list[el][name[i]]])
                graygrid.append(len(dataf))
                axl.set_ylabel(self.vis_label(el))
                axr.set_ylabel('Deviation (‰)')
        cycle = np.arange(0,len(dataf))
        for i in graygrid:
            if i % (graygrid[0] * 2) == 0:
                axl.axvspan(i-graygrid[0], i, color = "lightgrey")
        #axl.get_xaxis().set_major_locator(ticker.MultipleLocator(len(signals[0])*Tintegr))
        axl.tick_params(labelbottom=False)
        axl.plot(cycle,dataf,'ko',markersize=2)
        if el in self.cup_element:
            axr.set_ylim(100*min(axl.get_ylim())/mean(axl.get_ylim())-100,100*max(axl.get_ylim())/mean(axl.get_ylim())-100)
        elif el in self.ir_list:
            axr.set_ylim([(val/mean(axl.get_ylim())-1)*1000 for val in axl.get_ylim()])
        axl.tick_params(bottom='False',left='False',right='False',top='False',labelbottom='False')
        axl.set_xlim(min(cycle),max(cycle))
        axl.locator_params(axis='y',nbins=8);axr.locator_params(axis='y',nbins=8)
        axl.grid(axis='y')
        axr.grid(axis='y',linestyle='dashed')
        #plt.tight_layout()
        plt.show()
        plt.close()

    def box_vis(self,el,name):
        vis_params()
        dataf = pd.DataFrame({})
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if el in self.cup_element:
            for i in range(len(name)):dataf[name[i]] = self.dataset[name[i]][self.cup_element.index(el)]
            sns.boxplot(data=dataf, showfliers=False, ax=ax)
            sns.stripplot(data=dataf, jitter=True, color='black', ax=ax)
            plt.ylabel('Intensity of '+self.vis_label(el)+' / V')
        elif el in self.ir_list:
            for i in range(len(name)):dataf[name[i]] = self.ir_list[el][name[i]]
            sns.boxplot(data=dataf, showfliers=False, ax=ax)
            sns.stripplot(data=dataf, jitter=True, color='black', ax=ax)
            plt.ylabel(self.vis_label(el))
        plt.show()
        plt.close()

    def three_isotope_vis(self,xaxis,yaxis):
        plt.figure(figsize=(10,7))
        vis_params()
        fraction    = (self.element.info(yaxis.split('/')[0])-self.element.info(yaxis.split('/')[1]))/(self.element.info(yaxis.split('/')[0])*self.element.info(yaxis.split('/')[1]))
        denominator = (self.element.info(xaxis.split('/')[0])-self.element.info(xaxis.split('/')[1]))/(self.element.info(xaxis.split('/')[0])*self.element.info(xaxis.split('/')[1]))
        mfa = fraction / denominator
        x,y,xerr_list,yerr_list = [],[],[],[]
        for line in self.delta_list:
            x.append(self.delta_list[line][xaxis])
            xerr_list.append(2*self.delta_SE_list[line][xaxis])
            y.append(self.delta_list[line][yaxis])
            yerr_list.append(2*self.delta_SE_list[line][yaxis])
        plt.errorbar(x,y,xerr=xerr_list, yerr=yerr_list,fmt='ko',ecolor='black',capsize=3.0)
        plt.xlabel('δ'+self.vis_label(xaxis)+' (‰)')
        plt.ylabel('δ'+self.vis_label(yaxis)+' (‰)')
        xmfa = np.array(plt.xlim())
        ymfa = xmfa * mfa
        plt.plot(xmfa,ymfa,color='black')
        plt.grid(color='lightgray')
        #plt.tight_layout()
        plt.gca().set_xticklabels(['{:g}'.format(x) for x in plt.gca().get_xticks()])
        plt.gca().set_yticklabels(['{:g}'.format(x) for x in plt.gca().get_yticks()])
        #plt.show()
        #plt.close()
        pdf = PdfPages('three_isotope_plot.pdf')
        pdf.savefig()
        pdf.close()

    def vis_label(self,axis):
        try:
            clabel = axis.replace(re.sub("\\D", "", axis.split('/')[0]),u''.join(dict(zip(u"0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹")).get(c, c) for c in re.sub("\\D", "", axis.split('/')[0]))).replace(re.sub("\\D", "", axis.split('/')[1]),u''.join(dict(zip(u"0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹")).get(c, c) for c in re.sub("\\D", "", axis.split('/')[1])))
        except IndexError:
            clabel = axis.replace(re.sub("\\D", "", axis),u''.join(dict(zip(u"0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹")).get(c, c) for c in re.sub("\\D", "", axis)))
        return clabel

class nu2_geochronology():
    def __init__(self):
        pass

    def mode_select():
        print('Please select isotopic correctino mode !')
        print('1 : U-Pb zircon (glass)')
        print('2 : Pb-Pb zircon (glass)')
        print('3 : U-Pb zircon (mineral)')
        print('4 : Pb-Pb zircon (mineral)')

class attom:
    def __init__(self):
        self.filepath = os.getcwd()+'/RunNo.csv'

    def run_no(self):
        if os.path.exists(self.filepath) == True:
            run_no = open('RunNo.csv','r')
        else:
            run_no = open('RunNo.csv','w')
            print('Please input Run No.')
            data_list = [i for i in glob.glob('raw_data/*') if not '.py' in i and not '.txt' in i and not '.csv' in i]
            if 'data' in data_list:del data_list[data_list.index('data')]
            if 'figure' in data_list:del data_list[data_list.index('figure')]
            data_list = sorted(data_list)
            for i in data_list:
                id = input(i+' : ')
                run_no.write(','.join([i,id+'\n']))
            run_no.close()
            print('RunNo.csv > .')
            run_no = open('RunNo.csv','r')

    def binary2txt(self):
        jobid = 1
        data_list = [i for i in glob.glob('raw_data/*') if not '.py' in i and not '.txt' in i and not '.csv' in i]
        data_list = sorted(data_list)
        if 'data' in data_list:del data_list[data_list.index('data')]
        if 'figure' in data_list:del data_list[data_list.index('figure')]
        for fname in data_list:
            fi = open(fname,'r').readlines()
            fo = open(fname.split('.')[0]+'.txt','w')
            for line in fi:fo.write(line)
            print(pycolor.RED+'JOB_id = data '+str(jobid)+' '+pycolor.END+fname.split('.')[0]+'.txt > '+pycolor.BLUE+'data'+pycolor.END)
            jobid += 1
            fo.close()
        data_list = [i for i in glob.glob('*.txt')]
        data_list = sorted(data_list)
        filepath = os.getcwd()+'/data'
        if os.path.exists(filepath) == False:os.system('mkdir data')
        os.system('mv raw_data/*.txt data')

    def txt2png(self):
        jobid = 1
        filepath = os.getcwd()+'/data/*.txt'
        data_list = [i for i in glob.glob(filepath)]
        data_list = sorted(data_list)
        for fname in data_list:
            fi,frag = open(fname,'r').readlines(),0
            for line in fi:
                if 'Timestamp' in line:array = np.array(line.rstrip().split(','))
                if frag >= 10:array = np.vstack((array,np.array(line.rstrip().split(','))))
                frag += 1
            x = [float(i) for i in array.T[0][1:]]
            for j in range(len(array.T)-2):
                name = fname.split('/')[-1].split('.')[0] + '_' + array[0][j+2]
                y = [float(i) for i in array.T[j+2][1:]]
                self.genpng(x,y,name)
                print(pycolor.RED+'JOB_id = plot '+str(jobid)+' '+pycolor.END+name+'.png > '+pycolor.BLUE+'figure'+pycolor.END)
                jobid += 1
        filepath = os.getcwd()+'/figure'
        if os.path.exists(filepath) == False:os.system('mkdir figure')
        os.system('mv *.png figure')

    def genpng(self,x,y,name):
        plt.figure()
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.size'] = 10
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.major.width'] = 1.0
        plt.rcParams['ytick.major.width'] = 1.0
        plt.rcParams['lines.linewidth'] = 0.8
        plt.grid(which='major',color='lightgray',linestyle='-')
        plt.grid(which='minor',color='lightgray',linestyle='-')
        plt.plot(x,y,color='black')
        plt.title(name)
        plt.xlabel('Cycle')
        plt.ylabel('cps')
        plt.savefig(name+'.png')
        plt.close()

    def txt2xlsx(self):
        wb = xlwt.Workbook()
        for sheetname in glob.glob('data/*.txt'):
            sheet = wb.add_sheet(sheetname.split('/')[1].split('.')[0])
            line, row = 0, 0
            for i in open(sheetname).readlines():
                i = i.split(',')
                for j in range(len(i)):
                    sheet.write(line, j, i[j])
                line += 1
            print(pycolor.GREEN + 'OK : '+pycolor.BLUE + sheetname)
        wb.save('attom_data.xls')
        print(pycolor.REVERCE)
        print(pycolor.BLUE+'attom_data.xls')

class icap:
    def __init__(self):
        print('Sorry, now constructing...!')
