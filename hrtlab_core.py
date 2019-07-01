import csv
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
