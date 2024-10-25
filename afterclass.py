def reverse_bits(n, bit_size=32):
    reversed_num = 0
    
    for i in range(bit_size):
        lsb = n & 1
        reversed_num = (reversed_num << 1) | lsb

        n = n >> 1
    
    return reversed_num

number = int(input("Enter a number: "))

reversed_number = reverse_bits(number)

print(f"Reversed bits formed the number: {reversed_number}")
