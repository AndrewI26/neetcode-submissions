'''
. . .
slow fast medium
10s 5s 7.5s
stack = [7.5]
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        closest_to_target = [(speed[i], position[i]) for i in range(len(position))]
        closest_to_target.sort(key=lambda item: item[1], reverse=True)

        time_to_target = [(target - pos) / speed for (speed, pos) in closest_to_target]

        res = 0
        last_time = -1
        for time in time_to_target:
            if time > last_time: 
                res += 1
                last_time = time

        return res