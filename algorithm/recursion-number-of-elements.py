def recur_numbers(l):
  if not l:
    return 0
  else:
    return recur_numbers(l[:1]) + len(l[0])

def main():
  print(recur_numbers(5))


if __name__ == '__main__':
  main()