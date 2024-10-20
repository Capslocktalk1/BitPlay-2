def printTwoOdd(arr, size):
    xorof2 = arr[0]
    x = 0
    y = 0
    setbit = 0
    
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
        
    setbit = xorof2 & ~(xorof2 - 1)
    
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
            
    print("the odd elements are ", x, "&", y)
    
arr = []

n = int(input("enter array size: "))

for i in range(0, n):
    num = int(input())
    arr.append(num)
    
printTwoOdd(arr, n) 