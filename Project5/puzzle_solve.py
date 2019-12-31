#project 5
import sys

def puzzle_solve():

	fList = open(sys.argv[1]).readlist()
	f.close()

	listNew = []

	for x in range(4, len(fList), 3):
		mult = fList[x]*10
		if mult > 255:
			mult = 255
		fList[x+1] = fList[x+2] = mult
		listNew.append(mult)
	
	h = open('hidden.py', 'w')
	h.write(P3/n)
	h.write(500, 375/n)
	h.write(255/n)
	for item in listNew:
		h.write("%s/n" % item)
	h.close()

	return hidden.py





