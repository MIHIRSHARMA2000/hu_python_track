from itertools import combinations
from collections import Counter


class StringClass:

    # init method or constructor
    def __init__(self, str):
        self.str = str

    # Sample Method
    def LengthOfString(self):
        counter = 0
        for i in self.str:
            counter += 1
        return counter

    def ConvertStringToCharacters(self):
        return list(self.str)


class PairsPossible(StringClass):
    def __init__(self, str1):
        self.str1 = str1

    def AllPossiblePairs(self):
        res = list(combinations(self.str1, 2))

        print("All possible pairs : " + str(res))


def SearchCommonElements(StringClass):
    def commonelement(self):
        d = dict(Counter(list(self.str)))
        ans = []
        for j in d:
            if d[j] >= 2:
                ans.append(j)
        return ans


Obj = StringClass('12314532')
print(Obj.LengthOfString())
print(Obj.ConvertStringToCharacters())
Obj1 = PairsPossible('12314532')
print(Obj1.AllPossiblePairs())
Obj2=SearchCommonElements()
print(Obj2.commonelements())
