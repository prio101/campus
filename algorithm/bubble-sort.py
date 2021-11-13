arr = [12,11,13,15,14]

def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr)-2):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp 
def main():
  bubble_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()