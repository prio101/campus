arr = [11,12,10,8,9]

def selection_sort(arr):
  size = len(arr)
  for step in range(size):
    min_place = step

    for index in range(step+1, size):
      if arr[index] < arr[min_place]:
        min_place = index
      temp = arr[step]
      arr[step] = arr[min_place]
      arr[min_place] = temp  

def main():
  selection_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()