#1 Biggie Size
# given a list, change all positive numbers to the str "big"
def biggie_size(lis):
    for x in range(len(lis)):
        if type(lis[x]) == str:
            continue
        if lis[x] > 0:
            lis[x] = "big"
    return lis
print(biggie_size([-1,3,5,-5,1324,-55,0,2,-12, "biggieTrip"]))

#2 Count Positives
# given a list, create function to replace last value with the number of positive values
def count_positives(lis):
    count = 0
    for x in range(len(lis)):
        if lis[x] > 0:
            count = count + 1
    lis[len(lis)-1] = count
    return lis
print(count_positives([1,6,-4,-2,-7,-2]))

#3 Sum Total
# given a list, return the sum of all values in array
def sum_total(lis):
    sum = 0
    for x in range(len(lis)):
        sum = sum + lis[x]
    return sum
print(sum_total([6,3,-2]))

#4 Average
# given a list, return the average of all values
def average(lis):
    avg = 0
    for x in range(len(lis)):
        avg = avg + lis[x]
    avg = avg/len(lis)
    return avg
print(average([1,2,3,4,-9,0,100]))

#5 Length
# given a list, return length of list
def length(lis):
    l = len(lis)
    return l
print(length([37,2,1,-9,1,3,5,6,-223,12,63434]))

#6 Minimum
# given a list, return min value; if list is empty, return False
def minimum(lis):
    if len(lis) < 1:
        return False
    min = lis[0]
    for x in range(len(lis)):
        if lis[x] < min:
            min = lis[x]
    return min
print(minimum([37,2,1,-9]))

#7 Maximum
# given a list, return max value; if list is empty, return False
def maximum(lis):
    if len(lis) < 1:
        return False
    max = lis[0]
    for x in range(len(lis)):
        if lis[x] > max:
            max = lis[x]
    return max
print(maximum([37,2,1,-9]))

#8 Ultimate Analysis
# given a list, return dictionary with sumTotal, average, minimum, maximum and length of list
def ultimate_analysis(lis):
    ua = {}
    ua['sumTotal'] = sum_total(lis)
    ua['average'] = average(lis)
    ua['minimum'] = minimum(lis)
    ua['maximum'] = maximum(lis)
    ua['length'] = length(lis)
    return ua
print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List
# given a list, return list with values reversed
def reverse_list(lis):
    orig = len(lis)
    for x in range(len(lis)):
        lis.append(lis[orig-1-x])   #first we append the new values
    for y in range(orig):
        lis.pop(orig-1-y)           #then we pop the old
    return lis
print(reverse_list([1,2,3,4,5,6,7,8,9,10]))
