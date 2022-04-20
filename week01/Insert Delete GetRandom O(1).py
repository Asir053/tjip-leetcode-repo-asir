class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.ls = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        ind = self.dict[val]
        self.ls[ind] = self.ls[-1]
        self.dict[self.ls[-1]] = ind
        self.ls.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.ls)

