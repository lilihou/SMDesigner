import os
import re
from pathlib import Path
data_fold1=Path('./seq_struc_riboswitch')
data_fold2=Path('./seq_struc_riboswitch1')
finame=os.listdir(data_fold1)
for i in finame:
    print(i)
    fi=open(data_fold1/i,'r')
    fo=open(data_fold2/i,'w')
    for line in fi.readlines():
        if '#=GC SS_cons' in line:
            ls=line.split()
            ls_seq='#=GC SS_cons'
            line1=re.sub('[\{\[\(]','<',ls[-1])
            line2=re.sub('[\}\]\)]','>',line1)
            line3=f'{ls_seq:<45}'+re.sub('[\_\-\:\~]','.',line2)+'\n'
            fo.write(line3)
        elif '#=GC cov_SS_cons' in line:
            ls_id='#=GC cov_SS_cons'
            line4=f'{ls_id:<45}'+line.strip().split()[-1]+'\n'
            fo.write(line)
        elif '#=GF NUM_COV' in line:
            fo.write(line)
        elif not line:
            pass
        else:
            fo.write(line)

            
