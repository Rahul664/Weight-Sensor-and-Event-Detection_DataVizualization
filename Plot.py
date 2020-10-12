# Created by RAHUL S H on 10/09/20
#!/usr/bin/env python
# coding: utf-8

#Import library section
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


cwd=os.getcwd()
# cwd
files_in_cwd=os.listdir(path=cwd)
# files_in_cwd
csv_files_in_cwd=[]
for i in files_in_cwd:
    try:
        if(i.split(".")[1]=="csv"):
            csv_files_in_cwd.append(i)
    except:
        pass
# csv_files_in_cwd= [i for i in files_in_cwd if(i.split(".")[1]=="csv")]
# csv_files_in_cwd

for i in csv_files_in_cwd:
    try:
        
        file_name=i
        df_csv=pd.read_csv(str(file_name),delimiter=",",header=0)
        # Group data by 'timestamp','gondola','shelf' and perform aggregate operation to sum the readings
        grouped_data=df_csv.groupby(['timestamp','gondola','shelf']).agg({'reading':['sum']})
        grouped_data=grouped_data.reset_index()#reset index to get the colums back

        # Group data by 'gondola and shelf after summing weights
        gondola_shelf_data=grouped_data.groupby(['gondola','shelf'])
        try:
            os.mkdir(cwd+"/"+str(i.split(".")[0]))
        except:
            pass
        path_to_file=cwd+"/"+str(i.split(".")[0])
        
        for gondola in range(1,4):
            for shelf in range(1,7):
                try:
                    g_sh=pd.DataFrame(gondola_shelf_data.get_group((float(gondola),float(shelf))))
                    g_sh['ma']=g_sh['reading'].rolling(window=61,min_periods=61).mean()
                    g_sh['mv']=g_sh['reading'].rolling(window=61,min_periods=61).var(ddof=0)
                    x=g_sh['timestamp']

                    x=x-x.iloc[0]

                    y=g_sh['reading']

                    y1=g_sh['ma']
#                     y2=g_sh['mv']

                    plt.figure(figsize=(30,4))
                    plt.plot(x,y,'-b',label='Aggregated weight',linewidth=.35)
                    plt.plot(x,y1,'--r',label="Moving average",linewidth=2)
                    plt.xlabel("Timestamp (in seconds)")
                    plt.ylabel("Weight Sensor Reading (in grams)")
                    plt.title("Gondola "+str(gondola)+" "+"Shelf "+str(shelf)+" "+str(i))
                    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
                    plt.ioff()
                    plt.savefig(str(path_to_file)+"/"+str(gondola)+","+str(shelf)+".png")
                except:
                    pass
    except:
        pass



