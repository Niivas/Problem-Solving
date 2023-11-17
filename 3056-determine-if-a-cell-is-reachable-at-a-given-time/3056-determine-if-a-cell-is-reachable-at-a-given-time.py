class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_distance = abs(sx-fx)
        y_distance = abs(sy-fy)
        min_dist = min(x_distance,y_distance) + abs(y_distance - x_distance)
        if min_dist == 0: 
            if t == 1:
                return False
            else:
                return True
        return t >= min_dist
