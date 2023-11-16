import os
import re
#####################from CRS test3_CRS_22-3-31.py
#<<<.<.<.<...<<.<.<.<...<<.<.<.<.<<..<<.<<..<..<..<<<.......>>.>..>..>...>>.>>.......<<.<.<......<.<..<.<..<.........<<.<<..<.......>>>.>>.<..<<<<.........>>.>.>..>.<<.........<<.<<<....<<.<<.<......<<...<..<<<.........>.>>...>..>..>....>.>>....>.>.......<<...<...<.<.<....>>.>.>.>>..<.<.<.<.<..<.<..<<.........>>..>..>.>.>...>.>.......>...>>>...>..>.>>..>..>.>.>>...>>>>....<<<<........<<<..<.<.<.......<<<<<........>>>>>.....>.>>...>.>..>......>...>.....>>...<<.<.<..<..<.<.<......>.>>..>..>.>..>.>.....>>>>.>>>...>.....>>.>>.>..>.>.>>>....

#string='....<<<....<<<<<<<....>>>>>>>..<<..<<<..>>><<<..>>>..>>...>>>.'
#....333333333333333333333333333222222222222111111112222333333.
#........111111111111111111..........
#....333333333333333333333333333222222222222111111112222333333.
#....<<<....<<<<<<<....>>>>>>>..<<..<<<..>>><<<..>>>..>>...>>>.

def laopo(string):
	ls_loop=[]
	ls_loop1=[]
	ls_stem=[]
	ls_struc=[]
	ls_string=[]
	num9=string.index('<')
	#print('num9:',num9)
	num10=len(string)
	while num10!=1 and string[num10-1]!='>':
		num10-=1 
	num10=num10-1
	#print('num10',num10)
	while re.search('<\.+>',string):
		str5=''
		str4=''
		nu=re.search('<\.+>',string).span()
	#num9=nu[1]-nu[0]
		ls_loop.append([nu[0],nu[1]-1])
		for k in range (nu[1]-nu[0]-2):
				str4=str4+'_'
			#print(str4)
			#str5='<'+str4+'>'
			
			#str5='<'+str4+'>'
		#print(str4)
		str5='<'+str4+'>'
		string=re.sub('<\.+>', str5, string,1)
		#string_mu=

	#print('ls_loop:',ls_loop)
	#print('string:',string)
	#print(string)

	for i in range(len(ls_loop)):
		j=ls_loop[i][1]
		k=ls_loop[i][0]
		num7=0
		num8=0
		if i ==0:
			
			while string[j]!='<' and j<num10:
				j+=1
				if string[j]=='>':
					num7+=1
			while k>=num9:
				k-=1
				if string[k]=='<':
					num8+=1
			#print(num7,num8)
		elif i== len(ls_loop)-1:
			
			while j<num10:
				j+=1
				if string[j]=='>':
					num7+=1
			while string[k]!='>':
				k-=1
				if string[k]=='<':
					num8+=1
		elif 0<i<len(ls_loop)-1:
			
			while string[j]!='<':
				j+=1
				if string[j]=='>':
					num7+=1
			while string[k]!='>':
				k-=1
				if string[k]=='<':
					num8+=1
		num_temp=ls_loop[i][0]
		num_temp1=ls_loop[i][1]	
		#print(num_temp,num_temp1,num7,num8)
		if num7<=num8:
			num7_temp=num7
			
			while num7>0:
				num_temp-=1	
				if string[num_temp]=='<':
					num7-=1
			while num7_temp>0:	
				num_temp1+=1
				if string[num_temp1]=='>':
					num7_temp-=1	
			#print(num_temp,num_temp1) 
			
		else:
			num8_temp=num8
			while num8>0:
				num_temp-=1	
				if string[num_temp]=='<':
					num8-=1
			while num8_temp>0:	
				num_temp1+=1
				if string[num_temp1]=='>':
					num8_temp-=1	
		#print(num7,num8)
		ls_loop1.append([num_temp,num_temp1])
			
	#print('ls_loop1:',ls_loop1)
	#print(len(ls_loop),len(ls_loop1))
	#string_stem=string
	#string_mu=
	for k in range(len(string)):
		num=1
		for m in range(len(ls_loop1)):
			if ls_loop1[m][0]<=k<=ls_loop1[m][1] and string[k] in ['>','<']:
				ls_stem.append(str(m))
				num=0
		if num==1:
			ls_stem.append(string[k])
	

	num_stem=0
	num_stem1=0
	ls_temp=[]
	for k in range(len(string)):
		if k<num9:
			ls_struc.append('5s')
		elif k>num10:
			ls_struc.append('3s')
		elif string[k]=='_':
			ls_struc.append('p')
		else:
			if num9<=k<ls_loop1[0][0] or ls_loop1[len(ls_loop1)-1][1]<k<=num10:
					
				ls_struc.append(string[k])


			else:
				if len(ls_loop1)==1:
					if ls_loop1[0][0]<=k<=ls_loop[0][0]:
						if string[k]=='<':

							num_stem+=1
							ls_struc.append(str(num_stem)+'L')
							ls_temp.append(str(num_stem)+'L')
						elif string[k]=='.':
							ls_struc.append('B')
						num_stem1=len(ls_temp)
						#print(num_stem1)
					elif ls_loop[0][1]<=k<=ls_loop1[0][1]:
						if string[k]=='>':						
							ls_struc.append(str(num_stem1)+'R')
							num_stem1-=1
						elif string[k]=='.':
							ls_struc.append('B')
				elif len(ls_loop1)>1:
					for m in range(len(ls_loop1)-1):
						#if ls_loop[m][0]<k<ls_loop[m][1]:
							#ls_struc.append('p')
						if ls_loop1[m][0]<=k<=ls_loop[m][0]:
							if string[k]=='<':

								num_stem+=1
								ls_struc.append(str(num_stem)+'L')
								ls_temp.append(str(num_stem)+'L')
							elif string[k]=='.':
								ls_struc.append('B')
							num_stem1=len(ls_temp)
							#print(num_stem1)
						elif ls_loop[m][1]<=k<=ls_loop1[m][1]:
							if string[k]=='>':						
								ls_struc.append(str(num_stem1)+'R')
								num_stem1-=1
							elif string[k]=='.':
								ls_struc.append('B')
						elif ls_loop1[m][1]<k<ls_loop1[m+1][0]:
							ls_struc.append(string[k])
					if ls_loop1[-1][0]<=k<=ls_loop[-1][0]:
						if string[k]=='<':
							num_stem+=1
							ls_struc.append(str(num_stem)+'L')
							ls_temp.append(str(num_stem)+'L')
						elif string[k]=='.':
							ls_struc.append('B')
						num_stem1=len(ls_temp)
					elif ls_loop[-1][1]<=k<=ls_loop1[-1][1]:
							if string[k]=='>':						
								ls_struc.append(str(num_stem1)+'R')
								num_stem1-=1
							elif string[k]=='.':
								ls_struc.append('B')
				#else:
				#num_stem1=len(ls_stem)		#ls_struc.append(string[k])
	same_stem='/'.join(ls_stem)
	Mutation_struc='/'.join(ls_struc)
	return(same_stem,Mutation_struc)

def add_infor(ls,n,ls1,n1):
	str_len=len(ls)
	num=str_len-1
	num_stem=0
	num_stem1=0
	ls_l_po=[]
	ls_r_po=[]
	while str_len>=0 and ls[num]!='<':
		num-=1
		
	num_star=num
	#print(num_star)
	while num_star>=0 and ls[num_star]!='>':
		
		if ls[num_star]=='<':
			num_stem+=1
			ls_l_po.append(num_star)
		num_star-=1
	len_stem_l=num_stem
	#print(len_stem_l)
	num_star1=num+1
	while num_star1<str_len and ls[num_star1]!='<':
		if ls[num_star1]=='>':
			num_stem1+=1
			ls_r_po.append(num_star1)
		num_star1+=1
	len_stem_r=num_stem1
	#print(len_stem_r)
	if len_stem_l>len_stem_r:
		ls_l_po=ls_l_po[0:len_stem_r]
	else:
		ls_r_po=ls_r_po[0:len_stem_l]
	
	
	for i in ls_l_po:
		ls[i]=str(n)
	for j in ls_r_po:
		ls[j]=str(n)

	ls_l_po=ls_l_po[::-1]
	for i in ls_l_po:
		ls1[i]=str(n1)+'L'
		n1+=1
	length=n1-1
	for j in ls_r_po:
		ls1[j]=str(length)+'R'
		length-=1
	num2=n1-1
	return(ls,n,ls1,num2)

def count_stem(line):	
	num_com=0
	num_conser=0
	num_pair=0
	num_cov=0
	for i in line:
		if i=='1':
			num_com+=1
		elif i=='0':
			num_conser+=1
		elif i=='?':
			num_pair+=1
		elif i=='2':
			num_cov+=1

	num_all_pair=num_com+num_conser+num_pair+num_cov
	stem_count=str(num_com//2)+'_'+str(num_conser//2)+'_'+str(num_all_pair//2)
	return(stem_count)
#same_stem=add_infor(string,1)

filename=os.listdir("./seq_struc_riboswitch1/")
foo=open('no_struc_ribo.txt','w')
for ff in filename:
	print(ff)
	fi=open("./seq_struc_riboswitch1/"+ff,"r")
	j=ff.strip()[0:-9]+".seqStrucAdd"
	fo=open("./seq_struc_riboswitch1_add/"+j,"w")
	ls_file=fi.readlines()
	ls_seq={}
	ls_num=[]
	#print(ff)
	for line in ls_file:
		a=re.findall('^#=GC SS_cons|#=GC cov_SS_cons|#=GF NUM_COV',line)
		if line=="\n":
			pass
		#elif 'refseqgene' in line:
			#str_seq=line.split()[-1]	
			#seq=str_seq.replace('-','')
			#ls_seq[line.strip()]=len(seq)
		elif not a:

			str_seq=line.split()[-1]
			seq=str_seq.replace('.','')
			ls_seq[line.strip()]=len(seq)
		elif a:
			if '#=GC SS_cons' in line:
				#fo.write(line)
				ls_id2='#=GC SS_cons'

				line4=f'{ls_id2:<46}'+line.strip().split()[-1]+'\n'
				ls=line.strip().split()
				str1=ls[-1]
				same_stem,Mutation_struc=laopo(str1)
				ls_ss=same_stem.split('/')
				ls1=Mutation_struc.split('/')
				ls_num=[]
				ls_num1=[]
				for i in ls_ss:
					if i.isdigit():
						ls_num.append(int(i))
				for j in ls1:
					if 'L' in j:
						ls_num1.append(int(j[0:-1]))

				n=max(list(set(ls_num)))
				n1=max(list(set(ls_num1)))
				num_try=0
				while '<' in ls_ss and num_try<=5:
					num_try+=1
					n+=1
					n1+=1
					ls_ss,n,ls1,n1=add_infor(ls_ss,n,ls1,n1)
				string1='same_stem'
				string2='mutation_struc'
				line1=f'{string1:<46}'+''.join(ls_ss)+'\n'
				line2=f'{string2:<46}'+'/'.join(ls1)+'\n'
					
				#fo.write(line1)
				#fo.write(line2)
			elif '#=GC cov_SS_cons' in line:
				#'#=GC cov_SS_cons                             .....?2202........2..22.22?.......................................................................................?22.2.2.2222...022?2?.........................................?2?....220.222....................................................2022?...222?....................................................?222.................'
				#fo.write(line)	
				ls3=line.strip().split()
				line5_id=ls3[0]+' '+ls3[1]
				line5=f'{line5_id:<46}'+ls3[2]+'\n'
				string3='stem_count'
				line3=f'{string3:<46}'+count_stem(line)+"\n"
				#fo.write(line3)
			else:
				line6=line
	ls_num_seq = sorted(ls_seq.items(),key=lambda x:x[1],reverse = False)
	#print(ls_num)
	num_seq=0
	for k in range(len(ls_num_seq)):
		if 20<ls_num_seq[k][1]:
			num_seq+=1
			ls2=ls_num_seq[k][0].split()
			#print(ls)
			seq_id=ls2[0]+'_'+str(ls_num_seq[k][1])
			sequence=ls2[-1]
			refseq=f'{seq_id:<46}'+sequence+'\n'
			fo.write(refseq)
	fo.write(line4)
	fo.write(line1)
	fo.write(line5)
	#fo.write(line)
	fo.write(line2)
	fo.write(line3)
	fo.write(line6)
	if num_seq==0:
		ff=ff.strip()[0:-9]+".seqStrucAdd"+'\n'
		foo.write(ff)


#print(same_stem,Mutation_struc)
#././././</</</././././0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/././</</././1/1/1/1/1/1/1/1/2/2/2/2/2/2/2/2/././>/>/./././>/>/>/.
#5s/5s/5s/5s/</</</././././1L/2L/3L/4L/5L/6L/7L/p/p/p/p/7R/6R/5R/4R/3R/2R/1R/././</</././8L/9L/10L/p/p/10R/9R/8R/11L/12L/13L/p/p/13R/12R/11R/././>/>/./././>/>/>/3s

#print(''.join(ls))
#print(''.join(ls1))
