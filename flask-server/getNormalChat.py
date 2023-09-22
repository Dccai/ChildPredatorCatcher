import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\USER\Downloads\train.csv")
#0 is not groomer, 1 is groomer
print(df.iloc[:,2])
db=pd.read_csv(r"C:\Users\USER\Downloads\pedoChatLogs.txt", delimiter='\t', header=0, encoding='utf-8')
print(db)