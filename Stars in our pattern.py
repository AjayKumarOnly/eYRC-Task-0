def main():
  t = int(input())
  if 1 <= t <= 25:
        for _ in range(t):
          n = int(input())
          if 1 <= n <= 100:
              pat = star(n)
              for row in pat:
                print(row)
          else:
              print("")
  else:
      print("Enter the t value between 1 to 25")
      
def star(n):
  pat = []
  for i in range(n, 0, -1):
    row = ""
    for j in range(i):
      if (j + 1) % 5 == 0:
        row = row + "#"
      else:
        row = row + "*"
    pat.append(row)
  return pat

main()
