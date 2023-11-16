import os
import re
from pathlib import Path
data_fold1='/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/riboswitch_sto1/'
data_fold2='/home/lijuanh/projects/def-jonatp/lijuanh/riboswitch_mu_design/seq_struc_riboswitch/'
filename=os.listdir(data_fold1)
foo=open('no_struc_ribo.txt','w')

for i in filename:
	fi=open(data_fold1+i,"r")
	j=i.strip()[0:-9]+".seqStruc"
	fo=open(data_fold2+j,"w")
	ls=fi.readlines()
	num1=0
	num2=0
	ls_uni_seq=[]
	for line in ls:
		if line.startswith('#'):
			a=re.findall('^#=GF ',line)
			e=re.findall('^#=GF NUM_COV',line)
			b=re.findall('^#=GS |#=GR ',line)
			c=re.findall('^#=GC con|#=GC col|#=GC RF',line)
			d=re.findall('# STOCKHOLM 1.0|//',line)

			if b or c or d:
				continue
			elif a and not e:
				continue
			else:
				if re.findall('#=GC SS_cons',line):
					if ">" not in line:
						foo.write(i)


				#ls_anntate=[]
				ls_uni_seq.append(line.strip())
				#fo.write(line)
		else:

			#009|FN667741.1/3471117-3471071/1-47
			#LCLP01000004.1/37559-37400/1-151            AGUUU
			if '|' not in line:
				if '//' in line or line.isspace():
					pass
				else:
					seq_ls1=line.strip().split()
					#print(seq_ls1)
					seq1=f'{seq_ls1[0]:<45}'+seq_ls1[-1]
					ls_uni_seq.append(seq1)
			else:
				ls1=line.strip().split('|')
				seq=ls1[1]
				if seq in ls_uni_seq:
					pass
				else:
					seq_ls=seq.split()
					seq=f'{seq_ls[0]:<45}'+seq_ls[-1]
					ls_uni_seq.append(seq)
	for j in ls_uni_seq:
		line1=j+'\n'
		fo.write(line1)
			
