import random

# cases to consider
# adjacency ( left node and right node )

def generate_matrix(n):
  main_array = []

  for item in range(0,n):
    sub_arr = []
    for _ in range(0, n):
      input = random.randint(0, 1000)
      sub_arr.append({ item:  input })
    
    main_array.append(sub_arr)
    
  
  print("your generated matrix is: ")
  print(main_array)
  return main_array


def maximum_sum_sub_matrix(main_array):
  pass
  # 1. if i == ir+1 or ir-1 and valid or
  # 2. if i == ic+1 or ic-1 and valid then
  # 3. edge case = last row and first row should not visit null rows
  # 4. edge case = last col and first col should not visit null cols

  for item in range(len(main_array)):
    length = len(main_array)
    
    maximum_sum_sub_matrix_result = 0;

    # edge case 3 and 4
    if item <= 0 and item >= length:
      return maximum_sum_sub_matrix_result

    # edge case 1 and 2 with other checking





def main():
  n = int(input("Enter the Number for the: NxN matrix"))
  main_array = generate_matrix(n)

  maximum_sum_sub_matrix(main_array)

if __name__ == '__main__':
  main()
