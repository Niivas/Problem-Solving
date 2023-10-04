def getMinMachines():
    pass


n = 5
start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 7]

intervals = [(1, 7), (3, 6), (6, 7), (8, 9), (9, 14)]

map_ = {}  # 1:9, 2:14, 3:7

for pair in intervals:
    s, e = pair[0], pair[1]
    found = False
    for m in map_:
        if map_[m] < s:
            map_[m] = e
            found = True
            break
    if not found:
        map_[len(map_) + 1] = e

print(len(map_))
