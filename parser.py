#import String
import os
import sys
from intersection_detect import type_road

text=open('map_ukhra.txt','r')
lines=text.readlines()
text_l=open('map/rec_ukhra.csv','w')
text_l.write('id,lat,long\n')
text_l.close()

k4=''
k5=''
k6=''
rec=[]
#print(lines[0])
l=len(lines)
cnt=0
i=0

while i+1<l:
	line=lines[i].split(' ')
	if len(line)>5:
#	print(line)
	#for k in line:
		if 'id=' in line[3] and 'uid' not in line[3]:
			l1=len(line[3])-2
			k1=line[3][4:l1]
			k4=k1
			#id.append(k1)

		if 'lat=' in line[4] and 'maxlat' not in line[4] and 'minlat' not in line[4] :
			#print("b",k)
			l1=len(line[4])-2
			k2=line[4][5:l1]
			k5=k2
			#lat.append(float(k1))
		if 'lon=' in line[5] and 'maxlon' not in line[5] and 'minlon' not in line[5]:
			#print("a",k)
			line[5].replace('/','')
			l1=len(line[5])-4
			k3=line[5][5:l1]
			k6=k3
	rec.append([k4,k5,k6])
			#long.append(float(k1))
	i+=1
l2=len(rec)
j=0

	#cnt=0
#text=open(name1,'a')
while j<l2-1:
	if rec[j]==rec[j+1]:
		del rec[j+1]
		l2-=1
		continue
	j+=1

#print(rec)

l3=len(rec)
text=open('map/rec_ukhra.csv','a')
k=0
while k<l3:

	print(rec[k][0]+" "+rec[k][1]+" "+rec[k][2])
	#if rec[k][0]!='' and rec[k][1]!='' and rec[k][2]!='':
	text.write(str(rec[k][0])+","+str(rec[k][1])+","+str(rec[k][2])+"\n")

	k=k+1
text.close()

#print(rec)
	#cnt+=1
	#line=lines[i].split(' ')
	#for k in line:
	#	if 'lat' not in k or 'lon' not in k:
	#		break
	#if 'lat' not in lines[i] or 'lon' not in lines[i]:
	#	continue
#print(id)

#print(lat)



	#else:
	#i+=1
	#	k=lines[i].index('id')
	#	id.append(lines[i][])