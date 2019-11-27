
"""
Created on Wed Nov 27 20:24:49 2019

@author: Angela Leenzae Edang
"""

''' We bare Bears ECE Board Exam '''

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

print('DataFrame 1: \n')
print(x)

#converting format
w = pd.melt(x, id_vars = ['Student'], 
            value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
p = w.rename(columns = {'variable' : 'Subjects', 'value' : 'Grades'})
q = p.sort_values('Student').reset_index().drop(columns = 'index')

print('\n')
print('DataFrame 2: \n')
print(q) 

