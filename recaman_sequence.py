# recaman_sequence.py
# Andrew Lounsbury
# 21/3/23
# Purpose: generate the Recaman sequence; https://www.youtube.com/watch?v=FGC5TdIiT9U

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# generates the sequence up to the n-th number
def generate_recaman(n):
    sequence = [0]
    already_visited = [0]
    curNum = 0
    j = 1
    while len(sequence) < n:
        if curNum - j >= 0 and curNum - j not in already_visited:
            already_visited.append(curNum - j)
            sequence.append(curNum - j)
            curNum -= j
        else:
            already_visited.append(curNum + j)
            sequence.append(curNum + j)
            curNum += j
        j += 1
    return sequence

sequence = generate_recaman(50)
print(sequence)

n = 1000
sequence = generate_recaman(n)
df1 = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(n):
    indices.append(i)

df1["index"] = indices
sns.scatterplot(x="index", y="Number", data=df1)
plt.show()

n = 10000
sequence = generate_recaman(n)
df2 = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(n):
    indices.append(i)

df2["index"] = indices
sns.scatterplot(x="index", y="Number", data=df2)
plt.show()

n = 100000
sequence = generate_recaman(n)
df3 = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(n):
    indices.append(i)

df3["index"] = indices
sns.scatterplot(x="index", y="Number", data=df3)
plt.show()