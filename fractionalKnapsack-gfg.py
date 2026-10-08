class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        valWt = []
        currentCapacity = capacity
        maxValue = 0
        for i in range(len(val)) :
            valWt.append([val[i], wt[i]])
        valWt.sort(key= lambda x: x[0]/ x[1], reverse= True)
        for i in range(len(valWt)) :
            value , weight = valWt[i]
            if(weight <= currentCapacity) :
                maxValue += value
                currentCapacity -= weight
            else:
                maxValue += value/ weight * currentCapacity
                break
        return maxValue