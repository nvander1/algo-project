import sys
import queue
from instrumentNode import treeNode


def main():
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    contents = contents.split()
    numNotes = contents[0]
    
    process(numNotes,contents[1:])


def process(numNotes, notes):
    items = queue.Queue()
    finalLevel = []
    count = 0
    for comb in n2f[int(notes[0])]:
        ins = trumpetNode([],1,comb,0)
        ins.getFingerings().append(comb)
        items.put(ins)
    while not items.empty():
        curr = items.get()
        count+=1
        if(curr.getIndex()<len(notes)-1):
           # print("eval: {}, note:{}".format(curr, curr.getIndex()))
            for comb in n2f[int(notes[curr.getIndex()])]:
                ins = trumpetNode(curr.getFingerings()[:],curr.getIndex()+1,comb,curr.getCost()+dist[comb][curr.getValue()])
                ins.getFingerings().append(comb)
                items.put(ins)
        else:
            #print("else eval: {}, note:{}".format(curr, curr.getIndex()))
            for comb in n2f[int(notes[curr.getIndex()])]:
                ins = trumpetNode(curr.getFingerings()[:],500,comb,curr.getCost()+dist[comb][curr.getValue()])
                ins.getFingerings().append(comb)
                finalLevel.append(ins)
    print(min(finalLevel,key=lambda x: x.getCost()))
    print("processed:{}, lowest level: {}, total nodes: {}".format(count,len(finalLevel),count+len(finalLevel)))

main()
