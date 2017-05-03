import sys
import queue
from timeit import default_timer as timer
from instrumentNode import treeNode
from optimal_fingerings import N2F, F2N, DIST



def process(numNotes, notes):
    items = queue.Queue()
    finalLevel = []
    for comb in N2F[notes[0]]:
        ins = treeNode([comb],1,comb,0)
        items.put(ins)
    index = 0
    while(index<len(notes)-1):
        choices = {}
        while not items.empty():
            curr = items.get()
            #print(curr)
            if curr.noteIndex < len(notes)-1:
                for comb in N2F[notes[curr.noteIndex]]:
                    ins = treeNode(curr.fingerings[:], curr.noteIndex+1, comb, \
                    curr.cost+DIST[(comb,curr.value)])
                    ins.fingerings.append(comb)
                    if comb in choices:
                        choices[comb].append(ins)
                    else:
                        choices[comb] = [ins]
            else:
                #print("else eval: {}, note:{}".format(curr, curr.getIndex()))
                for comb in N2F[notes[curr.noteIndex]]:
                    ins = treeNode(curr.fingerings[:], 500, comb,\
                    curr.cost+DIST[(comb,curr.value)])
                    ins.fingerings.append(comb)
                    if comb in choices:
                        choices[comb].append(ins)
                    else:
                        choices[comb] = [ins]
        for key in choices.keys():
            #print(choices[key])
            #print("selected: {}".format(min(choices[key],key= lambda x: x.cost)))
            items.put(min(choices[key],key= lambda x: x.cost)) 
        choices = {}
        index += 1
    final = []
    while not items.empty():
        final.append(items.get())
    #print(final)
    return min(final,key= lambda x: x.cost)







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
