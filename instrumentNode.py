class TreeNode:
    def __init__(self, fingerings, index, value, cost):
        self.fingerings = fingerings
        self.noteIndex = index
        self.value = value
        self.cost = cost
    def __str__(self):
        return "past fingerings: {}, cost: {}. current eval: {}, \
         current index: {}".format(self.fingerings, self.cost, self.value, self.noteIndex)
