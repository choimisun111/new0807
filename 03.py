import pandas as pd
data = {
    '이름': ['성준','유진','인영','미선'],
    '나이': [26, 26, 25, 24],
    '성별': ['남','여','여','여']
}
df = pd.DataFrame(data, index=['A', 'B', 'C','D'])
df.to_csv("./data.csv")
print(df)
#df.to.csv("./3조.csv")

