# coding: utf-8
birthes = pd.read_csv('birthrates.csv')
birthes
birthes.columns = ['year', 'month', 'day', 'gender', 'birth']
birthes['decade'] = 10 * (birthes['year'] // 10)
birthes.pivot_table('birth', index='decade', columns='gender', aggfunc='sum')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
birthes.pivot_table('birth', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year');
