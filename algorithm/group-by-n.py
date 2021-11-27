def group(arr):
  print("given set of the array: ", arr)
  temp_list = []
  group_maker_spice = 3 # base jumper
  group_maker_spice_special_case_second_row = 2
  result_list = []

  for item in arr:
    if item == 0 and len(arr) > group_maker_spice:
      # insert the first 3 in a group
      # temp_list.append(0)
      temp_list = arr[:group_maker_spice]
      print("first group: ",temp_list)
      result_list.append(temp_list)
      temp_list = [] # reset the temp list
      group_maker_spice = group_maker_spice_special_case_second_row # change to the second row
      del arr[0:4] #select and delete till the 3rd element  
    if item == 1 and len(arr) > group_maker_spice:
      temp_list = arr[:group_maker_spice]
      result_list.append(temp_list)
      temp_list = []
      del arr[0:1] # delete till 2nd element form list

    result_list.append(arr)  

    print("grouped into three seperate list: ", result_list)



def main():

  arr = list(range(1, 50))

  group(arr)



if __name__ == '__main__':
  main()