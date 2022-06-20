def triple(data):

    result = map(lambda x: 3 * x, data)
    return list(result)

print(triple([1,2,3]))
    
def map3(func, data1, data2, data3):
    result = map(func, data1, data2, data3)
    return list(result)

def func(data1,data2,data3):
    return data1 * data2 * data3

print(map3(func,[1, 2, 3], [10, 20, 30], [100, 200, 300]))

def map2(func, data1, data2):
    result = map(func,data1,data2)
    return list(result)

def func(data1, data2):
    return data1**data2

print(map2(func,[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))