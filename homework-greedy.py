
#homework problem
#Describe an efficient algorithm that, given a set {x1, x2, . . . , xn}of points
#on the real line, determines the smallest set of unit-length closed intervals that contains all of the
#given points. Argue that your algorithm is correct.

def min_unit_intervals(items):
    if not items:
        return 0

    items.sort()

    count = 1
    dest = items[0] + 1.0

    for i in range(1, len(items)):
        if items[i] <= dest:
            continue
        dest = items[i] + 1.0
        count += 1

    return count