
def min_max(arr):
  
  # sorting way
  arr.sort()
  min = arr[0]
  max = arr[len(arr) - 1]
  
  print("sorting way:")
  print("min is: ")
  print(min)
  print("max is: ")
  print(max)
  print("-----------")


  # searching way
  min_value = arr[0]

  max_value = arr[len(arr) -1 ]


  for item in range(len(arr)):
    
    temp = arr[item]

    if temp < min_value:
      min_value = temp
    else:
      max_value = temp
    
  print("searching way:")
  print("max_value:")
  print(max_value)
  print("min_value:")
  print(min_value)


def main():
  arr = [5,6,8,7,7,2]
  min_max(arr)


if __name__ == '__main__':
  main()