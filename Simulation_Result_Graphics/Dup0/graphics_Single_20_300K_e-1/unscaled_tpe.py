# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:07:50 2021

@author: jake_
"""

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
import csv

#read in event waits
with open(folder+'\\Site_timeline_'+configuration[s]+'_'+config_size[s]+'_'+temperature[s]+'_'+pressure[s]+'.csv',newline='') as site_timeline:
    timeline_reader=csv.reader(site_timeline,delimiter=',',quotechar='|')
    first=True
    for row in timeline_reader:
        
#read in event counts
with open(folder+'\\Site_timeline_'+configuration[s]+'_'+config_size[s]+'_'+temperature[s]+'_'+pressure[s]+'.csv',newline='') as site_timeline:
    timeline_reader=csv.reader(site_timeline,delimiter=',',quotechar='|')
    first=True
    for row in timeline_reader:
        
#read in event scaling
with open(folder+'\\Site_timeline_'+configuration[s]+'_'+config_size[s]+'_'+temperature[s]+'_'+pressure[s]+'.csv',newline='') as site_timeline:
    timeline_reader=csv.reader(site_timeline,delimiter=',',quotechar='|')
    first=True
    for row in timeline_reader:
            
# plot
#PlotOptions()
plt.figure(figsize=(8,4.8))

width = 0.3
ind = 0
yvals = []
ylabels = []
bar_vals = []

#plot Pd only events
for i in range(11):
    
    if f_wait[i]+r_wait[i] > 0:

        if f_wait[i]>0:
            plt.barh(ind-0.4, f_wait[i], width, color='r', log = True)
            bar_vals.append(f_wait[i])
        
        if r_wait[i] > 0:
            plt.barh(ind-0.7, r_wait[i], width, color='b', log = True)
            bar_vals.append(r_wait[i])
        
        ylabels.append(names[i])
        yvals.append(ind-0.55)
        ind = ind - 1
        
#CO ads events
COads_names=['CO-adsorption-top','CO-adsorption-bridge','CO-adsorption-hollow']
#average ads across site types
CO_ads=[0,0,0,0,0,0]
CO_event=[0,0,0,0,0,0]
for i in range(11,20):
    CO_ind=-1
    if(names[i].find("top")>1):
        CO_ind=0
    if(names[i].find("bridge")>1):
        CO_ind=1
    if(names[i].find("hollow")>1):
        CO_ind=2
        
    if f_wait[i]+r_wait[i] > 0 and CO_ind>=0:

        if f_wait[i]>0:
            CO_ads[2*CO_ind]=CO_ads[2*CO_ind]+f_wait[i]
            CO_event[2*CO_ind]=CO_event[2*CO_ind]+f_event[i]
            
        if r_wait[i] > 0:
            CO_ads[2*CO_ind+1]=CO_ads[2*CO_ind+1]+r_wait[i]
            CO_event[2*CO_ind+1]=CO_event[2*CO_ind+1]+r_event[i]

CO_wait=[]
for i in range(len(CO_ads)):
    if(CO_event[i]==0):
        CO_wait.append(0)
    else:
        CO_wait.append(CO_ads[i]/CO_event[i])
 
#plot CO ads
for i in range(3):
    
    if CO_wait[2*i]+CO_wait[2*i+1] > 0:

        if CO_wait[2*i]>0:
            plt.barh(ind-0.4, CO_wait[2*i], width, color='r', log = True)
            bar_vals.append(CO_wait[2*i])
        
        if CO_wait[2*i+1] > 0:
            plt.barh(ind-0.7, CO_wait[2*i+1], width, color='b', log = True)
            bar_vals.append(CO_wait[2*i+1])
        
        ylabels.append(COads_names[i])
        yvals.append(ind-0.55)
        ind = ind - 1
        
PdCO_diff_names=['Pd1(CO)_diffusion_L0','Pd2(CO)_diffusion_L0','Pd3(CO)_diffusion_L0','Pd4_3d(CO)_diffusion_L0']
#plot CO diff
for i in range(20,len(f_wait)):
    
    if f_wait[i]+r_wait[i] > 0:

        if f_wait[i]>0:
            plt.barh(ind-0.4, f_wait[i], width, color='r', log = True)
            bar_vals.append(f_wait[i])
        
        if r_wait[i] > 0:
            plt.barh(ind-0.7, r_wait[i], width, color='b', log = True)
            bar_vals.append(r_wait[i])
        
        ylabels.append(PdCO_diff_names[i-20])
        yvals.append(ind-0.55)
        ind = ind - 1

bar_vals = np.array(bar_vals)

log_bar_vals = np.zeros(len(bar_vals))
for i in range(len(bar_vals)):
    log_bar_vals[i]=np.log10(float(bar_vals[i]))
xmin = 10**np.floor(np.min(log_bar_vals))
xmax = 10**np.ceil(np.max(log_bar_vals))

plt.xticks(size=12)
plt.yticks(size=12)
plt.xlabel('Time per Event (s)',size=24)
plt.yticks(yvals, ylabels)
plt.xlim([xmin, xmax])
if zoom > xmin and zoom < 1:
    plt.xlim([zoom, xmax])
    
leg_labels=['Forward', 'Reverse']
plt.legend(leg_labels, bbox_to_anchor = (1.05, 1),loc= 'upper left', prop={'size':12},frameon=False)

ax = plt.gca()
ax.set_xscale('log')
leg = ax.get_legend()

leg.legendHandles[0].set_color('r')
leg.legendHandles[1].set_color('b')

plt.tight_layout()

if savefig:
    plt.savefig('event_waits_unscaled_avg.png'), bbox_inches = "tight", dpi=300)

else:
    plt.show()

plt.close()
