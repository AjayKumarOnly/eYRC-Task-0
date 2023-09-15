import math

def main():
    t = int(input())
    if 1 <= t <= 25:
        for _ in range(t):
            x1, y1, x2, y2 = map(int, input().split())

            if -100 <= x1 <= 100 and -100 <= x2 <= 100 and -100 <= y1 <= 100 and -100 <= y2 <= 100:                         
                distance = dis(x1, y1, x2, y2)
                # Format the distance to two decimal places
                print(f"Distance: {distance:.2f}")

def dis(x1, y1, x2, y2):
    ans = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return ans

main()
