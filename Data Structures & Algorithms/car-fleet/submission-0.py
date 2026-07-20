class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted([[position[i], speed[i]] for i in range(len(speed))], reverse=True, key=lambda pair: pair[0])

        time_to_finish = [(target - pair[0]) / pair[1] for pair in combined]

        print(time_to_finish)
        fleets = 0
        stack = []
        for time in time_to_finish:
            print(stack)
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack = [time]
                    fleets += 1
        return fleets + (len(stack) if stack else 0)

        