def OddOccurring(arr):
    result = 0
    for i in arr:
        result = result ^ i
    return result

arr = []

n = int(input("Enter array size: "))

while(n):
    num = int(input())
    arr.append(num)
    n-=1
    
print("Odd occurring number is: ", OddOccurring(arr))