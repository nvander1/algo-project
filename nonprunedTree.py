import sys
import queue
from timeit import default_timer as timer
from instrumentNode import treeNode
from optimal_fingerings import N2F, F2N, DIST


def process(numNotes, notes):
    items = queue.Queue()
    finalLevel = []
    count = 0
    for comb in N2F[notes[0]]:
        ins = treeNode([], 1, comb, 0)
        ins.fingerings.append(comb)
        items.put(ins)
    while not items.empty():
        curr = items.get()
        count += 1
        if curr.noteIndex < len(notes)-1:
            #print("eval: {}, note:{}".format(curr, curr.noteIndex))
            for comb in N2F[notes[curr.noteIndex]]:
                ins = treeNode(curr.fingerings[:], curr.noteIndex+1, comb, \
                curr.cost+DIST[(comb,curr.value)])
                ins.fingerings.append(comb)
                items.put(ins)
        else:
            #print("else eval: {}, note:{}".format(curr, curr.getIndex()))
            for comb in N2F[notes[curr.noteIndex]]:
                ins = treeNode(curr.fingerings[:], curr.noteIndex+1, comb,\
                curr.cost+DIST[(comb,curr.value)])
                ins.fingerings.append(comb)
                finalLevel.append(ins)
    return min(finalLevel, key=lambda x: x.cost) 
    #print("processed:{}, lowest level: {}, total nodes: {}".format(count,len(finalLevel),count+len(finalLevel)))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    contents = contents.split()
    numNotes = contents[0]
    for i in range(1,len(contents)):
        contents[i] = int(contents[i])
    #print(timeit.timeit('process(numNotes,contents[1:])',number=10))
    start = timer()
    bestNode = process(int(contents[0]),contents[1:])
    end = timer()
    print(end-start)
    print(bestNode)
