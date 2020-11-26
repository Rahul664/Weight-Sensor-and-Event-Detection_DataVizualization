#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import library section
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
from collections import OrderedDict
import sys
import csv
import os
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


# In[2]:


cwd=os.getcwd()
cwd
files_in_cwd=os.listdir(path=cwd)
files_in_cwd
csv_files_in_cwd=[]
for i in files_in_cwd:
    try:
        if(i.split(".")[1]=="csv"):
            csv_files_in_cwd.append(i)
    except:
        pass



# In[28]:


for i in csv_files_in_cwd:
    try:
        
        file_name=i
        df_csv=pd.read_csv(str(file_name),delimiter=",",header=0)
        # Group data by 'timestamp','gondola','shelf' and perform aggregate operation to sum the readings
        grouped_data=df_csv.groupby(['timestamp','gondola','shelf'])['reading'].sum()
        grouped_data=grouped_data.reset_index()#reset index to get the colums back

        # Group data by 'gondola and shelf after summing weights
        gondola_shelf_data=grouped_data.groupby(['gondola','shelf'])
        try:
            os.mkdir(cwd+"/"+str(i.split(".")[0]))
        except:
            pass
        path_to_file=cwd+"/"+str(i.split(".")[0])
        
        for gondola in range(1,6):
            for shelf in range(1,7):
                try:
                    event=[]
                    g_sh=pd.DataFrame(gondola_shelf_data.get_group((float(gondola),float(shelf))))
                    g_sh['ma']=g_sh['reading'].rolling(window=61,min_periods=61).mean()
                    g_sh['mv']=g_sh['reading'].rolling(window=61,min_periods=61).var(ddof=0)
                    
                    threshold=float(10000)
                    g_sh['check']=g_sh['mv']>threshold
                    g_sh_series=list(g_sh['check']) 

                    #Event detection logic
                    sliding_window=30
                    event_begin_arr=[]
                    event_end_arr=[]
                    cnt=[]
                    k=0
                    while( k <= len(g_sh_series)-sliding_window):
                        cnt.append(k)
                        if g_sh_series[k:k+sliding_window].count(True)==sliding_window:
                            event_begin_arr.append(k)
                            event_begin=k
                            for j in range(k+sliding_window,len(g_sh_series)):
                                if g_sh_series[j:j+sliding_window].count(False)==sliding_window:
                                    event_end_arr.append(j+sliding_window)
                                    event_end=j+sliding_window
                                    break
                                else:
                                    k+=1
                            if event_end>event_begin:
                                event.append([threshold,event_begin,event_end])
                                k=event_end
                            else:
                                k+=1
                        else:
                            k+=1
                    k=0
                    
                    a1="S"
                    b1="E"
                    x=list(i for i in range(len(g_sh['timestamp'])))
                    y=g_sh['reading']
                    y1=g_sh['ma']
                    
                    legend_elements = [ Line2D([0],[0], linestyle='-', color='b',lw=.35, label='Raw Shelf Weight'),
                                       Line2D([0],[0], linestyle='--', color='r',lw=3, label='Moving Average Shelf Weight'),
                                        Line2D( [0],[0],marker='o', color='w', label='Detected Event(s)',
                                              markerfacecolor='g', markersize=10),
                                       Line2D( [0],[0],marker='o', color='w', label='S=Event Start',
                                              markerfacecolor='g', markersize=10),
                                       Line2D( [0],[0],marker='o', color='w', label='E=Event End',
                                              markerfacecolor='g', markersize=10)]
                    
                    fig=plt.figure(figsize=(30,8))
                    plt.plot(x,y,'-b',linewidth=.35)
                    plt.plot(x,y1,'--r',linewidth=3)
                    
                    if len(event)!=0:
                        for i in range(len(event)):
                            x2=list(i for i in range(event[i][1]-30, event[i][2]))
                            y2=list(g_sh.iloc[event[i][1]-30: event[i][2]]['ma'])
                            plt.plot(x2,y2,'.g',linewidth=.35)
                            plt.annotate(str(a1),xy=(x2[0],y2[0]), fontsize=25)
                            plt.annotate(str(b1),xy=(x2[len(x2)-1],y2[len(y2)-1]), fontsize=25)   
                    plt.xticks(fontsize=25)
                    plt.yticks(fontsize=25)
                    
                    plt.xlabel("Timestamp (in seconds)",fontsize=25)
                    plt.ylabel("Weight Sensor Reading (in grams)",fontsize=25)
                    
                    plt.title("Gondola "+str(gondola)+" "+"Shelf "+str(shelf)+" "+str(file_name),fontsize=30)
#                     plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
                    plt.legend(handles=legend_elements, loc='upper right',prop={"size":15})
                    plt.ioff()
                    plt.savefig(str(path_to_file)+"/"+str(gondola)+","+str(shelf)+".png")
                    plt.close(fig)
                except:
                        pass
    except:
        pass


