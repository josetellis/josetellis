import pandas as pd
# dt=pd.read_csv("d://csvdata/data.csv")
# print(dt)
dt=['Mumbai','Chennai','Bangalore',[10,20,30]]
dt1={'Mumbai':34,'Chennai':25,'Bangalore':35}
df=pd.DataFrame(dt1,index=list('ABC'))
print(df)