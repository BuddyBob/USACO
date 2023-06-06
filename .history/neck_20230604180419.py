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
    seg = []
    #check to the right of bead -> all the way to end bead + beginning bead
    for b in beads[index:len(beads)]+beads[0:index]:
        #get closest -> non white bead
        if current == "w":
            for c in beads[index:len(beads)]+beads[0:index]:
                if c != "w":
                    current = c
        if b == current or b == "w": 
            max_temp += 1
            seg.append(b)
        else: 
            print("ERROR!: "+str(b))
            break
            
    print(str(seg)
    print("started: "+str(current)+" max_beads: "+str(max_temp)+" length of beads: "+str(len(seg))+"\n")
    index += 1

fout.write(str(max_beads) + "\n")
fout.close()
