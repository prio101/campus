
list = [1,2,3,4,5,6,7,8,9]

const group_by_n = (list) => {
  // same as before:
  let temp_list = []
  let group_base_spice = 3
  let group_base_spice_special_case_secon_row = 2
  let result_list = []

  for(item in list){
    if(item == 0 && list.length > group_base_spice){
      temp_list = list.splice(0, group_base_spice);
      result_list.push(temp_list);
      temp_list = [] // reset
      group_base_spice = group_base_spice_special_case_secon_row

    }
    if(item == 1 && list.length > group_base_spice){
      temp_list = list.splice(0, group_base_spice);
      result_list.push(temp_list);
      temp_list = []
      
    }

    result_list.push(list)
    
    console.log("this should show three seperate list:",result_list)
    return result_list;
  } 

}