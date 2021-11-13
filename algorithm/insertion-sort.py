
arr = [12,11,13,15,14]

def insertion_sort(arr):

  for step in range(1, len(arr)):
    key = arr[step]

    left = step - 1                               

    while left >= 0 and key < arr[left]:
      arr[left+1] = arr[left]
      left = left - 1
    
    arr[left+1] = key
      

def main():
  insertion_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()