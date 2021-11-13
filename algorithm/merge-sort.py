arr = [11,2,8,4,5,12]

def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)

    merge_sort(right)

    i = j = k =0

    while i < len(left) and j < len(right):
      if left[i] <  right[j]:
        arr[k] = left[i]
        i = i + 1
      else:
        arr[k] = right[j]
        j = j + 1
      k = k + 1

    while i < len(left):
      arr[k] = left[i]
      i = i + 1
      k = k + 1
    
    while j < len(right):
      arr[k] = right[j]
      j = j + 1
      k = k + 1


def main():
  merge_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()