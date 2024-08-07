import numpy
import numpy as np
import pandas as pd

my_index = ['A', 'B', 'C']
my_columns = ['.이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', '홍길동'],
                     [25,30,36],
                     ['남', '여','남']]). transpose()
df = pd.DataFrame(my_data, index= my_index, columns=my_columns)
#print(df[['나이','성별']])

print(df,df.loc["A"])


