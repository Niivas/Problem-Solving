class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupMap = defaultdict(list)

        for i,groupLen in enumerate(groupSizes):
            groupMap[groupLen].append(i)
        
        res = []

        for groupLen,persons in groupMap.items():
            group = []
            for person in persons:
                if len(group) == groupLen:
                    res.append(group)
                    group = []
                group.append(person)
            res.append(group)
        return res
