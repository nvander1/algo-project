class treeNode:
    def __init__(self,fingerings,index,value,cost):
        self.fingerings = fingerings
        self.noteIndex = index
        self.value = value
        self.cost = cost
    def getIndex(self):
        return self.noteIndex
    def getFingerings(self):
        return self.fingerings
    def getValue(self):
        return self.value
    def getCost(self):
        return self.cost
    def __str__(self):
        return "past fingerings: {}, cost: {}. current eval: {}, current index: {}".format(self.fingerings,self.cost,self.value,self.noteIndex)
