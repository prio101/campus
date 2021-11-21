
def take_input():
  print("Please enter the input for the digits:")
  str = input("Enter:")
  str
  return str

def even_odd(str):
  length = len(str)
  last_index = length - 1
  
  # modules Way:
  print("modulas way:")
  if int(str[last_index]) % 2 == 1:
    print("it is odd")
  else:
    print("it is even")

  # bitwise way:
  print("bitwise way:")
  if int(str[last_index])&1 == 1:
    print("it is odd")
  else:
    print("it is even")


def main():
  str = take_input()
  even_odd(str)

if __name__ == '__main__':
  main()