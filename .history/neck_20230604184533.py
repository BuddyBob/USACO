necklace = "rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr"
length = len(necklace)
necklace *= 2
maxes = []
for index, bead in enumerate(necklace[0: length]):
    firstStreak = 1
    i = 1
    while i < length and necklace[index + i] == bead or necklace[index + i] == "w" or bead == "w":
        if (bead == "w") and (necklace[index + i] != "w") :
            bead = necklace[index + i]
        i += 1
        firstStreak += 1
    print(firstStreak,necklace)
    secondStreak = 0
    while i < length and (necklace[index + i] != bead):
        i += 1
        secondStreak += 1
    maxes.append(firstStreak + secondStreak)
    
print(maxes)
print(max(maxes))