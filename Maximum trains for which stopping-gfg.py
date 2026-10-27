class Solution:
    def maxStop(self, m, trains):
        #code here
        output = {}
        sumMaxValue = 0
        #sort by departure
        trains.sort(key=lambda x: x[1])
        for train in trains:
            if train[2] not in output:
                 output[train[2]] = {'count': 1, 'start': train[0], 
                                            'departure': train[1]}
            else:
                dept = output[train[2]]['departure']
                if dept <= train[0]:
                    output[train[2]]['count'] += 1
                    output[train[2]]['departure'] = train[1]
        sumMaxValue = sum(value["count"] for value in output.values())
        return sumMaxValue