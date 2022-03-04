ranked = [1]
player = [1, 1]

merged = ranked + player
merged.sort(reverse=True)
newRank = []
denseRank = 1
j = len(player) - 1


for i in range(len(merged)):
    if j == -1:
        break
    if player[j] == merged[i]:
        newRank.append(denseRank)
        j -= 1
        continue
    if i == len(merged) - 1:
        break
    if merged[i] == merged[i + 1]:
        continue
    else:
        denseRank += 1

newRank.sort(reverse=True)
print(newRank)
