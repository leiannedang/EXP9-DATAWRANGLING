# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:51:25 2019

@author: 2ecea-7 - Angela Leenzae Edang
"""

''' We Bare Bears ECE Board Exam '''

import pandas as pd

#raw data
data1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Math': [80, 95, 79]} 
data2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Electronics': [85, 81, 83]}
data3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'GEAS': [90, 79, 93]}
data4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'ESAT': [93, 89, 88]}

#dataframes
bears1 = pd.DataFrame(data1, columns = ['Student', 'Math'])
bears2 = pd.DataFrame(data2, columns = ['Student', 'Electronics'])
bears3 = pd.DataFrame(data3, columns = ['Student', 'GEAS'])
bears4 = pd.DataFrame(data4, columns = ['Student', 'ESAT'])

#tidy_bears merge
z = pd.merge(bears1, bears2, how='right', on='Student')
y = pd.merge(z, bears3, how='right', on='Student')
x = pd.merge(y, bears4, how='right', on='Student')

print(x)
