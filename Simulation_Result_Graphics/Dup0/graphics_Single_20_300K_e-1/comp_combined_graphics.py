# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:09:16 2021

@author: jake_
"""


#imports
import numpy as np
import pandas as pd
import xlrd
import os
import sys
import math
import matplotlib as mat
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.patches as mpatches
from matplotlib.pyplot import cm
import csv

#run information
configuration = ['Single']    #Single or Pd4
config_size = ['20']
temperature = ['300K']
pressure = ['e-1']
timeframe = 60
savefig=True

#set up plot
plt.figure(figsize=(7,4.8))
    
ylab = 'CO/Pd Ratio'
xlab = 'Time (s)'
colors_pool = np.vstack(cm.viridis(np.linspace(0,1,len(configuration))))

plot_names=[]

#CO/Pd ratios
#loop through each sim
for s in range(len(configuration)):
    #read in data
    time=[]
    COPd_ratio=[]
    
    with open('Site_timeline_'+configuration[s]+'_'+config_size[s]+'_'+temperature[s]+'_'+pressure[s]+'.csv',newline='') as site_timeline:
        timeline_reader=csv.reader(site_timeline,delimiter=',',quotechar='|')
        first=True
        for row in timeline_reader:
            if not first:
                line=row
                time.append((float)(line[0]))
                COPd_ratio.append(((float)(line[8]))/((int)(line[1])+(int)(line[2])+(int)(line[3])+(int)(line[4])))
            else:
                first=False
    #plot sim
    # plot
'''
    plt.plot(time, COPd_ratio, linestyle='--', color = colors_pool[s % len(colors_pool)])
    plot_names.append(configuration[s]+'_'+config_size[s]+'_'+temperature[s]+'_'+pressure[s])
    
#format plot
if(timeframe==60):
    plt.xticks(np.arange(0,60.1,step=10))
#plt.yticks(size=20)
plt.xlabel(xlab, size=24)
plt.ylabel(ylab, size=24)
plt.xlim(0,timeframe)
plt.ylim(0)
plt.legend(plot_names, bbox_to_anchor = (1.02,1),loc= 'upper left', prop={'size':12}, frameon=False)
plt.tight_layout()

if savefig:
    plt.savefig('COPd_ratio_300.png', bbox_inches = "tight", dpi=300)

else:
    plt.show()
'''
plt.close()
