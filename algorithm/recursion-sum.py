def recursum(n):
  if( n <= 1):
    return n;
  return n + recursum(n-1)

def main():
  print(recursum(5))

if __name__ == '__main__':
  main()