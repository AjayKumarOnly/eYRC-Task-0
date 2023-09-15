def main():
  t = int(input("Enter the number of testcase::"))
  if 1 <= t <= 25:
    for i in range(t):
      str = input('Enter the words:')
      length = len(str)
      if 2 <= length <= 100:
        if palindrome(str):
          print("It is a palindrome")
        else:
          print("It is not a palindrome")
      else:
        print("The str length between 2 to 100")
  else:
    print("Enter the t value upto 5")

def palindrome(str):
  str = str.upper()
  str_reversed = str[::-1]
  return str == str_reversed
main()
