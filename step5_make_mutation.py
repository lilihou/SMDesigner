import os
import re

def cov_po(b):
	if b[-1]=='l':
		d=b[0:-1]+'r'
		return(d)
	elif b[-1]=='L':
		d=b[0:-1]+'R'
		return(d)
	elif b[-1]=='r':
		d=b[0:-1]+'l'
		return(d)
	elif b[-1]=='R':
		d=b[0:-1]+'L'
		return(d)

def multi_sub(string,p,c):
    new = []
    for s in string:
        new.append(s)
    for index,point in enumerate(p):
        new[point] = c[index]
    return ''.join(new)

def stem_num(s):
	import re
	ls=[]
	dic={}
	#str5=':::::::::::.::::1111.11111,,,,,,,,,,,,222--22222____22222--22233333333--33333_____..333333333333311111--1111:'
	str6=re.sub('[^1-9]','',s)
	for i in str6:
		ls.append(i)
	ls1=list(set(ls))
	for j in ls1:
		dic[j+'stem']=ls.count(str(j))/2
	dic=sorted(dic.items(), key=lambda item:item[1], reverse=True)

	return(dic)
#::11111--11111.-------11111-111_____111-11111--------11111--11111,,,,,,,,,,,,,,,,,,,,,2222-----22______22----2222--------00000---0000,,,,,,,,.,3333333.____________333-------3333,,,,,,,,,,,,,,,,.,,,,,,44-44444___________4444444,,,,,,,0000-00000::::::::::::::::::::::
#..1??0?..000?1........?1000.10?.....?01.0001?........1?000..?0??1.....................?1?0.....?2......2?....0?1?........?0???...00?1..........?02??0?.............?0?.......?20?.......................01.??001...........100??10.......1?00.???0?......................	
def modi_basepair(str4,str3o,str1): 
	ls=['CG','GC','AU','UA','GU','UG']
	ls1=['1','0','?','2']
	ls_com=str4.split('/')
	ls4=[]
	for i in range(len(str3o)):
		if str3o[i] in ls1:
			#print(i)
			n=ls_com[i]
			m=cov_po(n)
			j=ls_com.index(m)
			basepair=str1[i]+str1[j]
			if basepair not in ls:
				#print(basepair)
				#print(i,j)
				ls4.append('.')
			else:
				ls4.append(str3o[i])
		else:
			ls4.append(str3o[i])
	#str3=modi_basepair(str4,str3,str1)
	str3=''.join(ls4)
	return(str3)

def stem_cov_num(line1,line2):
	ls=[]  #stem_num
	ls1=[]
	ls_stem=['0','1','2','?']
	dic={}
	dic1={}
	dic2={}
	line=re.sub('[^0-9]','',line1)
	#line=1111111111111111111111111111111111112222222222220000000003333333333333344444444444444000000000
	for i in range(len(line)):
		if i<1:
			ls.append(line[i])
		else:
			if line[i] not in ls:
				ls.append(line[i])	
			else:
				pass
	
	for j in ls:
		num=0  #covariation
		num1=0  #lenth_stem
		com=0  #compatiable mutation
		conser=0
		stem=0  #consertive basepair
		for k in range(len(line2)):
			if line1[k]==j:
				#num1+=1
				if line2[k]=='2':
					num+=1
				elif line2[k]=='1':
					com+=1
				elif line2[k]=='0':
					conser+=1
				elif line2[k]=='?':
					stem+=1

				else:
					pass
		num1=num+com+conser+stem
		if num1/2>1:
			dic['stem'+j+'-'+str(int(num1/2))]=int(num/2)
			dic1['stem'+j+'-'+str(int(num1/2))]=int(com/2)
			dic2['stem'+j+'-'+str(int(num1/2))]=int(conser/2)
	dic=sorted(dic.items(), key=lambda item:item[1], reverse=True)
	dic1=sorted(dic1.items(), key=lambda item:item[1], reverse=True)
	dic2=sorted(dic2.items(), key=lambda item:item[1], reverse=True)
	return(dic,dic1,dic2)
#cov>1
def pick_stem(dic1):

	if len(dic1)==1:
		num2=dic1[0][0].split('-')[0][-1]
		return num2
	elif len(dic1)>1:
		if dic1[0][1]!= dic1[1][1]:
			num2=dic1[0][0].split('-')[0][-1]

		elif dic1[0][1]== dic1[1][1]:
			if dic1[0][0].split('-')[-1]>dic1[1][0].split('-')[-1]:
				num2=dic1[0][0].split('-')[0][-1]
			else:
				num2=dic1[1][0].split('-')[0][-1]
		return num2
def mu_po(num,str5,str3,str1,str4,num1):
	po=[]
	nt=[]
	p0=[]
	n0=[]
	p1=[]
	n2=[]
	dic={}
	ls1=['CG','GC','AU','UA','GU','UG']
	index=[]
	ls_com=str4.split('/')
	for i in range(len(str1)):
		
		if str5[i]==num and str3[i]==num1 and i not in index:
			n=ls_com[i]
			n1=cov_po(n)
			m=ls_com.index(n1)
			mu1=str1[i]+str1[m]
			if mu1 in ls1:

				po.append(i)	
				po.append(m)
				index.append(m)
				nt.append(str1[m])
				nt.append(str1[i])

	num=len(po)
	if num==4:
		p0=po
		n0=nt
		p1.append(p0[0])
		p1.append(p0[2])
		n2.append(n0[0])
		n2.append(n0[2])
		
	elif num>4:
		if (num/2)%2==0:
			num1=int(num/2)-2
			
		elif (num/2)%2==1:
			num1=int(num/2)-1
		p0.append(po[num1])
		p0.append(po[num1+1])
		p0.append(po[num1+2])
		p0.append(po[num1+3])
		n0.append(nt[num1])
		n0.append(nt[num1+1])
		n0.append(nt[num1+2])
		n0.append(nt[num1+3])
		p1.append(p0[0])
		p1.append(p0[2])
		n2.append(n0[0])
		n2.append(n0[2])
	return(p1,n2,p0,n0)	
#cov==1	
def mu_po1(num,str5,str3,str1,str4):
	po=[]
	nt=[]
	p0=[]
	n0=[]
	p1=[]
	n2=[]
	dic={}
	ls1=['CG','GC','AU','UA','GU','UG']
	index=[]
	ls_com=str4.split('/')
	for i in range(len(str1)):
		if str5[i]==num and str3[i]=='2' and i not in index:
			n=ls_com[i]
			n1=cov_po(n)
			m=ls_com.index(n1)
			mu1=str1[i]+str1[m]
			if mu1 in ls1:
				po.append(i)	
				po.append(m)
				index.append(m)
				nt.append(str1[m])
				nt.append(str1[i])
	dic1,dic2,dic3=stem_cov_num(str5,str3)
	#print(dic1)
	#([('stem2-3', 1), ('stem3-5', 1), ('stem0-4', 0), ('stem1-17', 0), ('stem4-7', 0)], 
#[('stem1-17', 4), ('stem4-7', 2), ('stem2-3', 1), ('stem0-4', 1), ('stem3-5', 0)], 
#[('stem1-17', 8), ('stem0-4', 3), ('stem4-7', 3), ('stem3-5', 2), ('stem2-3', 1)])
	for j in dic2:
		if j[0].split('-')[0][-1]==num:
			num_com=int(j[-1])
			#print(num_com)

	for k in dic3:
		if k[0].split('-')[0][-1]==num:
			num_conser=int(k[-1])
	if num_com>=1:
		for i in range(len(str1)):
			if str5[i]==num and str3[i]=='1':
				n=ls_com[i]
				n1=cov_po(n)
				m=ls_com.index(n1)
				mu1=str1[i]+str1[m]
				if mu1 in ls1:
					po.append(i)	
					po.append(m)
					#index.append(m)
					nt.append(str1[m])
					nt.append(str1[i])
					break
			else:
				pass
	elif num_com==0:
		if num_conser>=1:
			for i in range(len(str1)):
				if str5[i]==num and str3[i]=='0':
					n=ls_com[i]
					n1=cov_po(n)
					m=ls_com.index(n1)
					mu1=str1[i]+str1[m]
					if mu1 in ls1:
						po.append(i)	
						po.append(m)
						#index.append(m)
						nt.append(str1[m])
						nt.append(str1[i])
						break
		elif num_conser==0:
			for i in range(len(str1)):
				if str5[i]==num and str3[i]=='?':
					n=ls_com[i]
					n1=cov_po(n)
					m=ls_com.index(n1)
					mu1=str1[i]+str1[m]
					if mu1 in ls1:
						po.append(i)	
						po.append(m)
						#index.append(m)
						nt.append(str1[m])
						nt.append(str1[i])
						break
	p1.append(po[0])
	p1.append(po[2])
	n2.append(nt[0])
	n2.append(nt[2])
	return(p1,n2,po,nt)

#com==1
def mu_po2(num,str5,str3,str1,str4):
	po=[]
	nt=[]
	p0=[]
	n0=[]
	p1=[]
	n2=[]
	dic={}
	ls1=['CG','GC','AU','UA','GU','UG']
	index=[]
	ls_com=str4.split('/')
	for i in range(len(str1)):
		if str5[i]==num and str3[i]=='1' and i not in index:
			n=ls_com[i]
			n1=cov_po(n)
			m=ls_com.index(n1)
			mu1=str1[i]+str1[m]
			if mu1 in ls1:
				po.append(i)	
				po.append(m)
				index.append(m)
				nt.append(str1[m])
				nt.append(str1[i])
	dic1,dic2,dic3=stem_cov_num(str5,str3)
	#print(dic1)
	#([('stem2-3', 1), ('stem3-5', 1), ('stem0-4', 0), ('stem1-17', 0), ('stem4-7', 0)], 
#[('stem1-17', 4), ('stem4-7', 2), ('stem2-3', 1), ('stem0-4', 1), ('stem3-5', 0)], 
#[('stem1-17', 8), ('stem0-4', 3), ('stem4-7', 3), ('stem3-5', 2), ('stem2-3', 1)])
     
#111____111,,,,,,,,,,,2222______2222-333__________________333:::::
#00?....?00...........0?0?......?0?0.1??..................??1.....	
	for k in dic3:
		if k[0].split('-')[0][-1]==num:
			num_conser=int(k[-1])
	if num_conser>=1:
		for i in range(len(str1)):
			if str5[i]==num and str3[i]=='0':
				n=ls_com[i]
				n1=cov_po(n)
				m=ls_com.index(n1)
				mu1=str1[i]+str1[m]
				if mu1 in ls1:
					po.append(i)	
					po.append(m)
					#index.append(m)
					nt.append(str1[m])
					nt.append(str1[i])
					break
			else:
				pass
	elif num_conser==0:
		for i in range(len(str1)):
			if str5[i]==num and str3[i]=='?':
				n=ls_com[i]
				n1=cov_po(n)
				m=ls_com.index(n1)
				mu1=str1[i]+str1[m]
				if mu1 in ls1:
					po.append(i)	
					po.append(m)
					#index.append(m)
					nt.append(str1[m])
					nt.append(str1[i])
					break
	p1.append(po[0])
	p1.append(po[2])
	n2.append(nt[0])
	n2.append(nt[2])
	return(p1,n2,po,nt)
#conser==1
def mu_po3(num,str5,str3,str1,str4):
	po=[]
	nt=[]
	p0=[]
	n0=[]
	p1=[]
	n2=[]
	dic={}
	ls1=['CG','GC','AU','UA','GU','UG']
	index=[]
	ls_com=str4.split('/')
	for i in range(len(str1)):
		if str5[i]==num and str3[i]=='0' and i not in index:
			n=ls_com[i]
			n1=cov_po(n)
			m=ls_com.index(n1)
			mu1=str1[i]+str1[m]
			if mu1 in ls1:
				po.append(i)	
				po.append(m)
				index.append(m)
				nt.append(str1[m])
				nt.append(str1[i])
	dic1,dic2,dic3=stem_cov_num(str5,str3)
	#print(dic1)
	#([('stem2-3', 1), ('stem3-5', 1), ('stem0-4', 0), ('stem1-17', 0), ('stem4-7', 0)], 
#[('stem1-17', 4), ('stem4-7', 2), ('stem2-3', 1), ('stem0-4', 1), ('stem3-5', 0)], 
#[('stem1-17', 8), ('stem0-4', 3), ('stem4-7', 3), ('stem3-5', 2), ('stem2-3', 1)])
	
			#print(num_com)
	for i in range(len(str1)):
		if str5[i]==num and str3[i]=='?':
			n=ls_com[i]
			n1=cov_po(n)
			m=ls_com.index(n1)
			mu1=str1[i]+str1[m]
			if mu1 in ls1:
				po.append(i)	
				po.append(m)
				#index.append(m)
				nt.append(str1[m])
				nt.append(str1[i])
				break
	
	
	p1.append(po[0])
	p1.append(po[2])
	n2.append(nt[0])
	n2.append(nt[2])
	return(p1,n2,po,nt)

filename=os.listdir("./seq_struc_riboswitch1_add")
#fn=open('no_20_100_seq_motif.txt','r')
fm=open('no_struc_ribo.txt','r')
ls_name=[]
ls_name1=[]
#for line in fn.readlines():
	#ls_name.append(line.strip())
for line in fm.readlines():
	ls_name1.append(line.strip())
for i in filename:
	#if i not in ls_name:
		#print(i)
    if i not in ls_name1:
        print(i)
        fi=open("./seq_struc_riboswitch1_add/"+i,"r")
        j=i.strip()[0:-12]+".mu.fa"
        fo=open("./seq_struc_file_fa/"+j,"w")
        ls=fi.readlines()
        seq_mu_id=''
        ls_com=[]
        num_cov=0
        num_com=0
        num_conser=0
        dic=[]
        ls_str1=[]
        num_str1=0
        ls_seq_id=[]
        ls_seq_wild=[]
        ls_seq_mu_id=[]
        for line in ls:
            a=re.findall('^\w+\d+',line)
            b=re.findall('#=GC SS_cons',line)
            c=re.findall('#=GC cov_SS_cons',line)
            d=re.findall('mutation_struc',line)
            e=re.findall('#=GF NUM_COV',line)
            f=re.findall('same_stem',line)
            
            if a:
                #string.replace(oldvalue, newvalue, count)
                num_str1+=1
                ls=line.strip().split()
                seq_mu_id=ls[0]
                seq_id='>'+'w'+str(num_str1)+'_'+ls[0]+'\n'
                seq=ls[-1].replace('.','').replace('-','')+'\n'
                #fo.write(seq_id)
                #fo.write(seq)
                ls_seq_id.append(seq_id)
                ls_seq_wild.append(seq)
                ls_str1.append(ls[-1])
                ls_seq_mu_id.append(seq_mu_id)			
                
            elif b:
    #(((((--((,,,,,,,,,,,,,,,<<<--------<<<<<<<______________>>>>>>>>>>,,,,.
                str2=line.strip().split()[-1]
            elif c:
    #1????..??...............??2........??00?1?..............?1?00??2??.....
                str3o=line.strip().split()[-1]
                
            elif d:
    #1L/2L/3L/4L/5L/././6L/7L/./././././././././././././././8L/9L/10L/./././.
                str4=line.strip().split()[-1]
                ls_com=str4.split('/')

            #elif e:
    #4    2    8  13
                #ls_stem=line.strip().split()
                #num_cov=int(ls_stem[-4])
                #num_com=int(ls_stem[-3])
                #num_conser=int(ls_stem[-2])
                #num_all_pair=int(ls_stem[-1])
            elif f:
    #:::::::::::.::::1111.11111,,,,,,,,,,,,222--22222____22222--22233333333--33333_____..333333333333311111--1111:
                str5=line.strip().split()[-1]
                #dic=stem_num(str5)
                #[('3stem', 13), ('1stem', 9), ('2stem', 8)]
        #print(str1)
        #print(str2)
        #print(str3)
        #print(ls_com)
        for m in range(len(ls_str1)):
            str3=modi_basepair(str4,str3o,ls_str1[m])
            dic1=[]  #cov
            dic2=[]  #com
            dic3=[]  #conserve
            dic1,dic2,dic3=stem_cov_num(str5,str3)
            num_all_pair=0
            for i in dic1:
                num_all_pair+=int(i[0].split('-')[-1])
        
    #([('stem2-3', 1), ('stem3-5', 1), ('stem0-4', 0), ('stem1-17', 0), ('stem4-7', 0)], 
    #[('stem1-17', 4), ('stem4-7', 2), ('stem2-3', 1), ('stem0-4', 1), ('stem3-5', 0)], 
    #[('stem1-17', 8), ('stem0-4', 3), ('stem4-7', 3), ('stem3-5', 2), ('stem2-3', 1)])

            if num_all_pair>2:
                dic4={}
                for i in dic3:
                    key=i[0].split('-')[0]
                    dic4[key]=int(i[0].split('-')[1])

                dic4=sorted(dic4.items(), key=lambda item:item[1], reverse=True)

                if dic1[0][1]>1:
                    num2=pick_stem(dic1)
                    p1,n2,p0,n0=mu_po(num2,str5,str3,ls_str1[m],str4,'2')
                    
                elif dic1[0][1]==1:
                    num2=pick_stem(dic1)
                    p1,n2,p0,n0=mu_po1(num2,str5,str3,ls_str1[m],str4)
                elif dic1[0][1]==0:
                    if dic2[0][1]>1:
                        num2=pick_stem(dic2)
                        p1,n2,p0,n0=mu_po(num2,str5,str3,ls_str1[m],str4,'1')
                    elif dic2[0][1]==1:
                        num2=pick_stem(dic2)
                        p1,n2,p0,n0=mu_po2(num2,str5,str3,ls_str1[m],str4)
                    elif dic2[0][1]==0:
                        if dic3[0][1]>1:
                            num2=pick_stem(dic3)
                            p1,n2,p0,n0=mu_po(num2,str5,str3,ls_str1[m],str4,'0')
                        elif dic3[0][1]==1:
                            num2=pick_stem(dic3)
                            p1,n2,p0,n0=mu_po3(num2,str5,str3,ls_str1[m],str4)
                        elif dic3[0][1]==0:
        #[('stem1-17', 8), ('stem0-4', 3), ('stem4-7', 3), ('stem3-5', 2), ('stem2-3', 1)]
                            num2=dic4[0][0][-1]
                            if dic4[0][1]>1:
                                p1,n2,p0,n0=mu_po(num2,str5,str3,ls_str1[m],str4,'?')
                seq_mu1=multi_sub(ls_str1[m],p1,n2)+'\n'
                seq_mu2=multi_sub(ls_str1[m],p0,n0)+'\n'
            #seq_mu1=seq_mu.replace('-','')+'\n'
                seq_mu1_id=">"+'m'+str(m+1)+'_1'+'_'+ls_seq_mu_id[m]+'\n'
                seq_mu2_id=">"+'m'+str(m+1)+'_2'+'_'+ls_seq_mu_id[m]+'\n'
                fo.write(ls_seq_id[m])
                fo.write(ls_seq_wild[m])
                fo.write(seq_mu1_id)
                fo.write(seq_mu1.replace('.','').replace('-',''))
                fo.write(seq_mu2_id)
                fo.write(seq_mu2.replace('.','').replace('-',''))
            #fo.write(p1,n2,p0,n0)


