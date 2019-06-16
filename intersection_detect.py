import os
import pandas as pd
import sys

def type_road():
	#df=pd.read_csv('rec_azone.csv')
	name1="map/ukhra.csv"
	text=open(name1,'w')
	text.write('id,type\n')
	text.close()
	#name='rec_azone.csv'
	text=open('map_ukhra.txt','r')
	read=text.readlines()
	v=[]
	#print("g")
	l=len(read)
	z=''
	p=''
	i=0

	while i<l:
		line=read[i].split(' ')
		#print(line)
		#for j in line:
		#z=''
		#p=''
			#print(j)
			#print("k")
		if len(line)>5:
			if 'way' in line[2]:
				#print("l")
				l2=len(line[3])-2
				index=line[3][4:l2]
				z=index
			#print(line[4])
			if '<tag' in line[4]:
					#i+=1
					#print("c")
					line2=read[i].split(' ')
					if 'k="highway"' in line2[5]:
						road=line2[6][3:len(line2[6])-4]
						#print(road)
						p=road
		#if z!='' and p!='':
		v.append([z,p])

				
		i+=1
	#print(v)
	l2=len(v)
	j=0
	cnt=0
	text=open(name1,'a')
	while j<l2-1:
		if v[j]==v[j+1]:
			del v[j+1]
			l2-=1
			continue
		j+=1

	l3=len(v)
	k=0
	while k<l3:


		if v[k][0]!='' and v[k][1]!='':
			text.write(str(v[k][0])+","+str(v[k][1])+"\n")
		k+=1
	text.close()

def main():
	type_road()
main()