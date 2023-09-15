def main():
  t = int(input())
  if 1 <= t <= 25:
      for i in range(t):
        n = int(input())
        if 0 <= n <= 100:
            for i in range(n):
              if i == 0:
                print(i + 3, end="")
              else:
                  if i % 2 == 0:
                    print(" ",i * 2, end="")
                  else:
                    print(" ",i * i, end="")
              print("")
        else:
            print("Enter the n value between 0 to 30")
  else:
      print("Enter the value between 1 to 5")

if _name_ == "__main__":
  main()
