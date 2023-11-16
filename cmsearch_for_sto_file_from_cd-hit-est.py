import os
from pathlib import Path
data_fold1=Path('/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/riboswitch_cm')
data_fold2=Path('/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/CD_hit_1')
data_fold3=Path('/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/riboswitch_sto')
files=os.listdir(data_fold2)
for file in files:
	#cmscan [-options] <cmdb> <seqfile>
    #cmsearch --notextw -A homocm8593.cm.sto homocm8593.cm /home/public/genomes/animal_all_genomes/animal_all.fn
	#print(file)
    if file.startswith('RF') and file.endswith('.fa'):
        print(file)
        fa_cmdb=file.split('.')[0]
        fo=fa_cmdb+'.sto'
        command=f'cmsearch --cpu 8 --notextw -A {data_fold3/fo} {data_fold1/fa_cmdb} {data_fold2/file}'
        os.system(command)

	



