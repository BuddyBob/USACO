"""
ID: thavasa1
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
N = int(fin.readline().rstrip())
beads = fin.readline().rstrip()

def count_collected_beads(N, necklace):
    necklace += necklace  # Create two copies of the necklace

    max_beads = 0

    for break_pos in range(N):
        beads_count = 0
        current_color = ''

        # Collect beads from the left side of the break position
        for i in range(break_pos, -1, -1):
            if necklace[i] == 'w' or necklace[i] == current_color or current_color == '':
                beads_count += 1
                if current_color == '':
                    current_color = necklace[i]
            else:
                break

        current_color = ''
        # Collect beads from the right side of the break position
        for i in range(break_pos + 1, break_pos + N + 1):
            if necklace[i] == 'w' or necklace[i] == current_color or current_color == '':
                beads_count += 1
                if current_color == '':
                    current_color = necklace[i]
            else:
                break

        max_beads = max(max_beads, beads_count)

    return max_beads




# Calculate the maximum number of collected beads
if len(set(beads)) == 1:
    fout = open('beads.out', 'w')
    fout.write(str(len(beads)) + "\n")
    exit()

else:
    max_beads = count_collected_beads(N, beads)

fout.write(str(max_beads) + "\n")
fout.close()
