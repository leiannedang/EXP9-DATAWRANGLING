
"""
Created on Wed Nov 27 20:43:31 2019

@author: Angela Leenzae Edang
"""

''' Computing Volume of a Box using Length, Width and, Height Columns '''

import pandas as pd

#raw data
data = {'Box': ['Box1', 'Box1', 'Box1',
                 'Box2', 'Box2', 'Box2'],
        'Dimension': ['Length', 'Width', 'Height',
                      'Length', 'Width', 'Height'],
        'Value': [6, 4, 2, 5, 3, 4]} 

messy = pd.DataFrame(data, columns = ['Box', 'Dimension', 'Value'])
tidy = messy.pivot_table(index = 'Box', columns = 'Dimension', 
                         values = 'Value').reset_index()

print('Raw Data: \n')
print(messy)

#fixed data
tidy['Volume'] = tidy.Height*tidy.Length*tidy.Width

print('\n')
print('Fixed Data with Computed Volume: \n')
print(tidy) 