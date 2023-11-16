import os
from pathlib import Path
data_fold1='/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/Rfam_fa/'
data_fold2='/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/CD_hit_1/'
fi=open('/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/riboswitch_families.txt','r')
for line in fi.readlines():
	key=line.strip().split(' ')[0]
	fi_name=key+'.fa'
	command=f'cd-hit-est -i {Path(data_fold1)/fi_name} -o {Path(data_fold2)/fi_name} -c 0.80 -M 0 -T 8'
	os.system(command)


#cd-hit -i /home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/Rfam_fa/RF01793.fa -o /home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/CD_hit/rf01793.fa -c 0.80 -M 0 -T 8

