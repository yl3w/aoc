# --- Day 4 : Repose record ----
#  https://adventofcode.com/2018/day/4
#  Invocation
#  sample - python repose_record.py sample.input
#  production - python repose_record.py production.input

from datetime import datetime
import itertools
import sys

def readSpecification(filename):
    """ Read the input file and return a time sorted list of tuples, Each tuple has 4 elements, 
    (a) seconds since beginning of year - used to sort the specs, (b) minute of the event
    (c) guard identifier (d) event (0 - begins shift, 1-wakes up, 2-falls asleep)"""
    boy = datetime(year=1518, month=1, day=1, hour=0, minute=0)
    msgWithSeconds = []
    with open(filename) as f:
        for line in f:
            date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            msg = line[19:]
            td = date - boy
            secondsElaspsed = int(td.total_seconds())
            msgWithSeconds.append((int(td.total_seconds()), date.minute, msg))

    msgWithSeconds.sort(key=lambda t: t[0])

    specs = []
    guard = -1
    for c in msgWithSeconds:
        event = -1
        msg = c[2].strip()
        if msg.startswith('Guard '):
            guard = int(msg[7:msg.index(' begins')])
            event = 0
        elif msg == 'wakes up':
            event = 1
        elif msg == 'falls asleep':
            event = 2
        else:
            raise ValueError('Unable to parse message "' + msg)

        specs.append((c[0], c[1], guard, event))
       

    return specs

def prepareSpecification(specs):
    """Takes the specification groups it by guard id, and sorts the list by minute"""
    specs.sort(key=lambda t: t[2])
    specsByGuard = {}
    for g, s in itertools.groupby(specs, key=lambda t: t[2]):
        specsByGuard[g] = sorted(list(s), key=lambda t: t[0])

    return specsByGuard

def computeTime(events):
    """Given a list of events, compute the sleep time"""
    mstamps = map(lambda t: t[1], filter(lambda t: t[3] != 0, events))
    return sum(map(lambda t: t[1] - t[0], zip(mstamps, mstamps)))


def computeTimeByGuard(specs):
    """ find the guard who has slept the most """
    return { k: computeTime(v) for k, v in specs.items() }

def findMostTiredGuard(sleepTimeByGuard):
    """find the guard with most sleep time, return tuple guard and time"""
    return max(sleepTimeByGuard.items(), key=lambda t: t[1])

def findMostFrequentMinute(events):
    """Given a list of events, find the minute with most sleep"""
    sleepFrequency = {}
    mstamps = map(lambda t: t[1], filter(lambda t: t[3] != 0, events))

    for t in zip(mstamps, mstamps):
        for minute in range(t[0], t[1]):
            sleepFrequency[minute] = sleepFrequency.get(minute, 0) + 1

    return max(sleepFrequency.items(), key=lambda t: t[1]) if len(sleepFrequency) > 0 else (-1, 0)

def findMostFrequentMinuteForAllGuards(specs):
    return { k : findMostFrequentMinute(v) for k, v in specs.items() }

def findMostVulnerableMinute(frequencies):
    return max(frequencies.items(), key=lambda t: t[1][1])

specs = prepareSpecification(readSpecification(sys.argv[1]))
sleepTimeByGuard = computeTimeByGuard(specs)

guard = findMostTiredGuard(sleepTimeByGuard)
print('Guard ' + str(guard[0]) + ' was the most tired guard, he was asleep for ' + str(guard[1]) + ' minutes')

sleepFrequency = findMostFrequentMinuteForAllGuards(specs)
print('Guard ' + str(guard[0]) + ' was most frequently asleep at ' + str(sleepFrequency[guard[0]][0]) + ' minute')

mvm = findMostVulnerableMinute(sleepFrequency)
print('Minute ' + str(mvm[1][0]) + ' is the most vulnerable. Guard ' + str(mvm[0]) + ' was asleep on this minute ' + str(mvm[1][1]) + ' times')
