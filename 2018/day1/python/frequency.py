fchanges = []
with open('frequency_input') as f:
	for line in f:
		fchanges.append(int(line))

current = 0
frequencies = []
for f in fchanges:
	current += f
	if current in frequencies:
		print('found duplicate in first cycle ' + str(current))
	frequencies.append(current)


print('Resulting skew is ' + str(current))
foundDuplicate = False
while not foundDuplicate:
	for f in fchanges:
		current += f
		if current in frequencies:
			print('found first repetition ' + str(current))
			foundDuplicate = True
			break


