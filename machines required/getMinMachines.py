def getMinMachines(start, end):
    intervals = list(zip(start, end))
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
    return len(map_)


intervalStart = [1, 3, 0, 5, 8, 5]
intervalEnd = [2, 4, 6, 7, 9, 9]

print(getMinMachines(intervalStart, intervalEnd))
