import pandas as pd 

df=pd.read_csv('map/8B.csv')
df2=pd.read_csv('map/rec_8B.csv')

lat=[]
long=[]
df_1=df2[df2.iloc[0]=]
l=len(df)
i=0

while i<l:
	k=df.iloc[i][0]
	j=0

	while j<len(df2):
		if k==df2.iloc[j][0]:
			print("a")
			lat.append(df2.iloc[j][1])
			long.append(df2.iloc[j][2])
			j+=1
			df2.drop([j])

			continue
		j+=1
	i+=1

df['lat']=lat
df['long']=long
print(long)

df.to_csv('map/rec_8B.csv',index=False)
