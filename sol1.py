#!/usr/bin/python

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

# Use hashmap O(n), return first result
def two_sum1(input, target):
    loopi = 1
    loopj = 1
    flag = 0
    # Creates an array of size 2 with elements [None]
    result = [None] * 2
    map = {}
    for i in input:
        # dict.get(i, 'default')
        if("default" == map.get(i, "default")):
            map[(target-i)] = loopi
        else:
            result[0] = map.get(i)
            result[1] = loopi
            return result
        loopi+=1
    return result

# Use hashmap O(n), return all the results
def two_sum2(input, target):
    loop = 1
    loop1 = 0
    result = []
    map = {}
    for i in input:
        if("default" == map.get(i, "default")):        
            map[target-i] = loop
        else:
            result.append([])
            result[loop1].append(map.get(i))
            result[loop1].append(loop)
            loop1+=1
        loop+=1
    return result

# @return a tuple, (index1, index2)
def twoSum(num, target):
  loop = 1

  # Creates an array of size 2 with elements [None]
  map = {}
  for i in num:
    # dict.get(i, 'default')
    if("default" == map.get(i, "default")):
      map[(target-i)] = loop
    else:
      index1 = map.get(i)
      index2 = loop
      return (index1,index2)
    loop+=1
  return (-1,-1)

input=[2, 7, 11, 15, 17, 27, 52, 7, 27]
target=34

print(twoSum(input, target))
print(two_sum(input, target))
print(two_sum1(input, target))
print(two_sum2(input, target))
