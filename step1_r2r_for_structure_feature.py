import os
from pathlib import Path
data_fold1=Path('./riboswitch_sto')

data_fold3=Path('./riboswitch_sto1')
files=os.listdir(data_fold1)
for file in files:
	
	#r2r --GSC-weighted-consensus homocm8593.cm.sto homocm8593.cons.sto 3 0.97 0.9 0.75 4 0.97 0.9 0.75 0.5 0.1
	fa_cmdb=file.split('.')[0]
	#fa_sto=fa_cmdb+'.sto'
	fo=fa_cmdb+'.cons.sto'
	command=f'r2r --GSC-weighted-consensus {data_fold1/file} {data_fold3/fo} 3 0.97 0.9 0.75 4 0.97 0.9 0.75 0.5 0.1'
	os.system(command)

	



