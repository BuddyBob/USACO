"""
ID: thavasa1
LANG: PYTHON3
TASK: beadsf
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
length = int(fin.readline().rstrip())
necklace = str(fin.readline().rstrip())*2
max_beads = 1

"""
wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
"""

index = 0
for current in necklace[:length]:
    max_temp = 0
    if len(set(necklace)) == 1:
        max_beads = length
        break
    #look to right of current split bead
    for b in necklace[index:]:
        #if current bead is white, set current to next non-white bead 
        if current == "w":
            for i in range(len(necklace)):
                if necklace[index+i] != "w":
                    current = necklace[index+i]
                    break
        #check how many beads to right of current bead are same color
        if b == current or b == "w":
            max_temp += 1
        else:
            break
        
    #look to left of current split bead (add end of necklace to front of necklace)
    for b in necklace[:index][::-1]:
        #if current bead is white, set current to next non-white bead 
        if b != current or b == "w":
            max_temp += 1
        else:
            break
    
    index += 1
    if max_temp > max_beads:
        max_beads = max_temp
    
fout.write(str(max_beads) + "\n")
fout.close()
