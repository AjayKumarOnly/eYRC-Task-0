def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n // 2)  
    print(n % 2, end='')  
T = int(input())


for _ in range(T):
    n = int(input())
    binary = bin(n)[2:]  
    binary = binary.zfill(8)   
    print(binary)
