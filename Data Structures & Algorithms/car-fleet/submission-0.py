class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk = []    
        for p, s in cars:
            time = (target - p) / s
            stk.append(time)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)