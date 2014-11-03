#!/usr/bin/python
input=[2, 7, 11, 15, 17, 27, 52]
target=34

# O(n^2) Naive solution
def two_sum(input, target):
    loopi = 1
    loopj = 1
    result = [None] * 2
    flag = 0

    for i in input:
        loopj = 1
        for j in input:
            if (i + j == target):
                result[0] = loopi
                result[1] = loopj
                flag = 1
                break
            loopj+=1
        loopi+=1
        if(flag == 1):
            break;

    return result

# Use hashmap O(n)
def two_sum1(input, target):
    loopi = 1
    loopj = 1
    result = [None] * 2
    flag = 0
    map = {}
    for i in input:
        # dict.get(i, 'default')
        if("default" == map.get(i, "default")):
            map[(target-i)] = loopi
        else:
            result[0] = map.get(i)
            result[1] = loopi
        loopi+=1
    return result

print two_sum(input, target)
print two_sum1(input, target)
