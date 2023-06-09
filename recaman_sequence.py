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

print(generate_recaman(100))

# Basic Scatterplots
n = 1000
sequence = generate_recaman(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/1000.png")
plt.show()

n = 10000
sequence = generate_recaman(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/10000.png")
plt.show()

n = 100000
sequence = generate_recaman(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/100000.png")
plt.show()

# Averages
n = 10
sequence = generate_recaman(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x = "index", y = "Average", data=df_average)
plt.savefig("images/average_10.png")
plt.show()

n = 100
sequence = generate_recaman(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x = "index", y = "Average", data=df_average)
plt.savefig("images/average_100.png")
plt.show()

n = 1000
sequence = generate_recaman(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x = "index", y = "Average", data=df_average)
plt.savefig("images/average_1000.png")
plt.show()

n = 10000
sequence = generate_recaman(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x = "index", y = "Average", data=df_average)
plt.savefig("images/average_10000.png")
plt.show()

n = 100000
sequence = generate_recaman(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x = "index", y = "Average", data=df_average)
plt.savefig("images/average_100000.png")
plt.show()