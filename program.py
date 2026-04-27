def plus_one(arr):
    num = int("".join(map(str, arr)))
    num = num + 1
    result = list(map(int, str(num)))
    return result

print(plus_one([1,2,3]))