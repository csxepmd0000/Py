# Author:csx
# -*- coding = utf-8 -*-
# @Time: AD 2023/04/08 15:57
# @File: 4-2.py
# @Software: PyCharm
import pandas as pd

data = [
    [160, 160],
    [161, 175]
]
nameOfLines = ['4月', '5月']
nameOfColumns = ['松田の労働(h)', '浅木の労働(h)']
df = pd.DataFrame(data, index=nameOfLines, columns=nameOfColumns)

print(df)

# 4-2
# print(type(df))
# print(df.shape)
