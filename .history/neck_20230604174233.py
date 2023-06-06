"""
ID: thavasa1
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
N = int(fin.readline().rstrip())
beads = fin.readline().rstrip()
max_beads = 1

index = 0
for bead in beads:
    max_temp = 0
    current = bead
    #check to the right of bead -> all the way to end bead + beginning bead
    for b in beads[index:len(beads)].extends(beads[0:index]):
        print(b,end="")
        if b == current or b == "w": max_temp += 1
        else: break
    
    
    
    
        
    print("\n")
    index += 1

fout.write(str(max_beads) + "\n")
fout.close()
