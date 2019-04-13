# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:04:39 2019

@author: Ksnnd Tngbrm
"""

in_file = 'dev_raw.csv'
out_file = 'dev_linked.csv'

with open(in_file, 'r') as in_file:
    rows = in_file.read().split('\n')
    
rows = rows[:195776]
    
with open(out_file, 'w') as out_file:
    for row in rows:
        sample_name = row.split(',')[0].split('/')[-1].split('.')[0]
        fea_file_name = 'train-feature/cv-valid/{}.csv'.format(sample_name)
        
        out_file.write('{},{}\n'.format(row, fea_file_name))
    