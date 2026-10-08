class Solution:
    def rotationCount(self, r: int, d: int) -> int:
        rotationCountVal = 0
        rString = str(r)
        dString = str(d)
        for i in range(len(rString)):
            rVal, dVal = int(rString[i]), int(dString[i])

            rotationCountVal += min(
                abs(rVal - dVal),
                abs(10  - rVal + dVal),
                abs(10 - dVal + rVal)
            )

        return rotationCountVal