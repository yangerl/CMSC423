fname = 'rosalind_ba5c.txt'
f = open(fname, 'r')
data = f.read().splitlines()
seq1 = data[0]
seq2 = data[1]
len1 = len(seq1)
len2 = len(seq2)
# Build scoring matrix L first
L = [[0 for x in range(0, len2+1)] for x in range(0, len1+1)]
for i in range(0, len1+1):
    for j in range(0, len2+1):
        if i == 0 or j == 0:
            L[i][j] = 0
        elif seq1[i-1] == seq2[j-1]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] = max(L[i-1][j], L[i][j-1])

index = L[len1][len2]
lcs = [""] * (index)

i = len1
j = len2

# Backtrack through scoring matrix
while i > 0 and j > 0:
    if seq1[i-1] == seq2[j-1]:
        lcs[index-1] = seq1[i-1]
        i-=1
        j-=1
        index-=1

    elif L[i-1][j] >= L[i][j-1]:
        i-=1
    else:
        j-=1

answer = open("answer.txt", 'w')
answer.write("".join(lcs))

 