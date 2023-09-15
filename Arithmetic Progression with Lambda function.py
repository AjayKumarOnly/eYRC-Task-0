from functools import reduce

# Function to generate A.P. series
def generate_AP(a1, d, n):
    ap_series = [a1 + (i * d) for i in range(n)]
    return ap_series

def main():
    T = int(input()) 
    for _ in range(T):
        a1, d, n = map(int, input().split())  
        ap_series = generate_AP(a1, d, n)

        squares = list(map(lambda x: x**2, ap_series))

        sum_of_squares = reduce(lambda x, y: x + y, squares)

        
        print(" ".join(map(str, ap_series)))
        print(" ".join(map(str, squares)))
        print(sum_of_squares)

    
main()
