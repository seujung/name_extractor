from __future__ import unicode_literals, print_function, division

import os
import re
import dill
import pandas as pd

PATTERN_LIST = []

def generate_pat(keyword, type, contain_space=True):
    if type == 'forward':
        if contain_space == True:
            return r'[0-9가-힣a-zA-Z]+(?={})|[0-9가-힣a-zA-Z]+(?= {})'.format(keyword, keyword)
        else:
            return r'[0-9가-힣a-zA-Z]+(?={})'.format(keyword)
    elif type =='backward':
        if contain_space == True:
            return r'(?<={})[0-9가-힣a-zA-Z]+|(?<={} )[0-9가-힣a-zA-Z]+'.format(keyword, keyword)
        else:
            return r'(?<={})[0-9가-힣a-zA-Z]+'.format(keyword)


patterns = pd.read_csv('name_rule.tsv', sep='\t')

for i in range(patterns.shape[0]):
    tmp_df = patterns.iloc[i]
    pat = generate_pat(tmp_df['keyword'], tmp_df['type'], tmp_df['contain_space'])
    PATTERN_LIST.append(pat)

with open('./name_pattern.pkl', 'wb') as f:
    dill.dump(PATTERN_LIST, f)