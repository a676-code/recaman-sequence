# recaman_sequence.py
# Andrew Lounsbury
# 21/3/23
sequence = [0]

# generates the sequence up to the n-th number
def generate(sequence, n):
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

generate(sequence, 20)
print(sequence)