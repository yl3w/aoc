import functools
import itertools

fchanges = []
with open('frequency_input') as f:
	for line in f:
		fchanges.append(int(line))

frequencies = [sum(fchanges[:index]) for index in range(1, len(fchanges)+1)]
skew = frequencies[-1]

print('Resulting skew is ' + str(skew))
accumulator = itertools.accumulate(itertools.cycle(fchanges))
prefix = itertools.takewhile(lambda x: (x + skew) not in frequencies, accumulator)
plen = functools.reduce(lambda x, y: x+1, prefix, 0)

accumulator = itertools.accumulate(itertools.cycle(fchanges))
print('found first repetition ' + str(next(itertools.islice(accumulator, plen, None)) + skew))
