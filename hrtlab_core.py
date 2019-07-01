import csv
import glob
import os
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

class nu2:
    def __init__(self,cup):
        self.cup = cup
        self.dataset = {}
        self.delta = {}

    def check_params(self):
        print('Cup : ',self.cup)

    def check_data(self,name):
        print(self.dataset[name])

    def get_data(self,name,cup):
        return self.dataset[name][self.cup.index(cup)]

    def data(self,data,name,id):
        if id == 'b':
            self.dataset[name] = self.read_blank(data)
        else:
            blank_list = [self.dataset[i] for i in id]
            blank = [sum(e)/len(e) for e in zip(*blank_list)]
            self.dataset[name] = self.read_sample(data,blank)

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
        for cupid in range(len(self.cup)):result.append(df[self.cup[cupid]+str(1)].mean())
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
        for cupid in range(len(self.cup)):result.append(df[self.cup[cupid]+str(1)] - blank[cupid])
        return result

    def calc_delta(self,std,spl):
        standard_5654 = std[1]/std[2]
        sample_5654 = spl[1]/spl[2]
        standard_5754 = std[0]/std[2]
        sample_5754 = spl[0]/spl[2]
        delta57 = ((sample_5754/standard_5754)-1)*1000
        delta56 = ((sample_5654/standard_5654)-1)*1000
        #print(sum(delta57)/len(delta57),sum(delta56)/len(delta56))
        return delta56

    def dot_vis(self,data,xlab,ylab):
        plt.figure()
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.size'] = 10
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.major.width'] = 1.0
        plt.rcParams['ytick.major.width'] = 1.0
        plt.rcParams['lines.linewidth'] = 0.8
        x = [i+1 for i in range(len(data))]
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.xlim(0,41)
        plt.scatter(x,data,s=20,c='black')
        plt.grid(which='major',color='lightgray',linestyle='-')
        plt.grid(which='minor',color='lightgray',linestyle='-')
        plt.show()

    def box_vis(self,name,el):
        sns.set()
        sns.set_style('white')
        sns.set_palette('Greys')
        dataf = pd.DataFrame({})
        for i in range(len(name)):dataf[name[i]] = self.dataset[name[i]][self.cup.index(el)]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        sns.boxplot(data=dataf, showfliers=False, ax=ax)
        sns.stripplot(data=dataf, jitter=True, color='black', ax=ax)
        plt.show()

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
