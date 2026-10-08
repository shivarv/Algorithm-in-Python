class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        
        # number of units in boxes
        # find max no of units in truck
        # truck size means total number of boxes it can keep

        # sort the list (added key=)
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        currentTruckSize = truckSize
        maxValue = 0

        for boxType in boxTypes:
            boxesCount, unitsPerBox = boxType[0], boxType[1]
            if boxesCount <= currentTruckSize:
                maxValue += (boxesCount * unitsPerBox)
                currentTruckSize -= boxesCount
            else:
                maxValue += currentTruckSize * unitsPerBox
                break
        return maxValue


# Unindented outside the class, with body indented properly
if __name__ == "__main__":
    solver = Solution()

    # Test inputs
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10

    result = solver.maximumUnits(boxTypes, truckSize)
    print("Result:", result)


#bucket sort better algo for the same since the constraint is 1001 buckets
def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # Step 1: Bucket array to hold box counts per unit size
        # Index represents units per box (up to max constraint 1000)
        unit_buckets = [0] * 1001

        for count, units in boxTypes:
            unit_buckets[units] += count

        max_units = 0

        # Step 2: Iterate greedily from the highest possible unit value down to 1
        for units in range(1000, 0, -1):
            if unit_buckets[units] == 0:
                continue

            # Take as many boxes as fit in the remaining truck capacity
            boxes_to_take = min(truckSize, unit_buckets[units])
            max_units += boxes_to_take * units
            truckSize -= boxes_to_take

            if truckSize == 0:
                break

        return max_units