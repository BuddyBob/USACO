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
    current = bead
    for b in beads[index:len(beads)]:
        print(b,end="")
        
    print("\n")
    index += 1

fout.write(str(max_beads) + "\n")
fout.close()
