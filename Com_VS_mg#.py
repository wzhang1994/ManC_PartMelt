#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

常见的岩石圈地幔组分(Griffin et al., 2009) 与 Mg#的关系 

结果显示
>91 - Arc
90-91 - Pro
<90 - Tc & DMM & PUM

@author: wzhang
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# 控制图像的格式
from matplotlib import rcParams	
plt.style.use('seaborn-whitegrid')
params={
        'figure.subplot.wspace' : 0.3,
        'axes.edgecolor' : 'black',        
        'axes.linewidth': 1,
        'lines.markersize' : 12,
        
        # 网格线
        'axes.grid': True,        
        'grid.color' : 'black',
        'grid.linewidth' : 0.5,
        'grid.linestyle' : '--',
        'legend.frameon' : True,
        'legend.fontsize' : 12,
        
        # 字体
        'font.family':'serif',
        'font.serif':'Arial', # 'Times New Roman'
        'font.style':'normal', # ‘normal’, ‘italic’ or ‘oblique’.
        'font.weight':'normal', #or ‘normal’ 'bold'
        'font.size':12,#or large,small 'medium'
        }
rcParams.update(params)


df = pd.read_excel(r"Composition.xlsx")
figname = "Com_VS_mg#.png"
print(df)


#fig = plt.figure(figsize=(12, 12), facecolor='white')
fig = plt.figure(figsize=(6, 6), facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)

annotate=0 # 是否标注名字
# ax1.plot(df['Mg#'], df['Density'], '.')
ax=ax1
X_label='MgO'
Y_label='TFeO'
for i in df.index:
	ann = df.loc[i]
	subfig, = ax.plot(ann[X_label], ann[Y_label], 
	marker=ann['Marker'], mfc=ann['Color'], mec=ann['Color'], linestyle=' ')
	
	# 点上的标注
	ax.annotate(ann['Name'], xy=(ann[X_label], ann[Y_label]),
	xytext=(1, 5), textcoords="offset points",		
	fontsize=10) if annotate >= 1 else None
	
	# ax.annotate(ann['Name'], xy=(ann[X_label], ann[Y_label]),
	# xytext=(1, 5), textcoords="offset points",		
	# fontsize=10) if ann['Name'] == 'DMM-3%' else None
    	# Legend setting
	subfig.set_label(ann['Name']) if ann['Name'] == 'PB_mant' else None
	subfig.set_label(ann['Name']) if ann['Name'] == 'ALCAPA' else None
	subfig.set_label('Archons (>2.5 Ga)') if ann['Name'] == 'Arc_1' else None
	subfig.set_label('Protons (1.0-2.5 Ga)') if ann['Name'] == 'Pr_1' else None
	subfig.set_label('Tectons (<1.0 Ga)') if ann['Name'] == 'Tc_2' else None
	subfig.set_label('DMM and its derivatives') if ann['Name'] == 'DMM' else None
	subfig.set_label('PUM') if ann['Name'] == 'PUM' else None

# The atomic weight of MgO and FeO
MgO_w=40.3044		# 24.305 + 15.9994 = 40.3044
FeO_w=71.8444 		# 55.845 + 15.9994 = 71.8444


MgO = np.arange(38,51)
# the line for Mg# = 90
mg_No = 90
FeO = (100/mg_No -1) * MgO/MgO_w * FeO_w
ax.plot(MgO, FeO, '--', label='Mg# = ' + str(mg_No))
# the line for Mg# = 90
mg_No = 91
FeO = (100/mg_No -1) * MgO/MgO_w * FeO_w
ax.plot(MgO, FeO, '--', label='Mg# = ' + str(mg_No))
plt.legend(loc='best', fontsize=8)

ax.set_xlabel(X_label+ ' ($wt\%$)')
ax.set_ylabel(Y_label+ ' ($wt\%$)')
# ax.set_xlim([89,93])

# ax.set_xlim([37,51])
# ax.set_ylim([6.0,10.0])

fig.savefig(figname,bbox_inches='tight', pad_inches=0.1,dpi=300)


