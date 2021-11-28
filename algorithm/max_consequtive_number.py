
# arr1 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

arr = [1,2,3,-1,-2,-3, 4, 5]

def max_subs_sum(arr):
  maximum_till_now = arr[0]
  maximum_ending_value = 0

  for item in range(0, len(arr)):
    maximum_ending_value = maximum_ending_value + arr[item]

    if(maximum_till_now < maximum_ending_value):
      maximum_till_now = maximum_ending_value
    if(maximum_ending_value < 0):
      maximum_till_now = maximum_ending_value
  
  print(maximum_till_now)


def main(arr):
  max_subs_sum(arr)

if __name__ == '__main__':
  main(arr)
