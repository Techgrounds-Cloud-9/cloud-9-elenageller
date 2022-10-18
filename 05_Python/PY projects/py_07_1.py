a_list = [1,2,3,4,5]
print("The list is :" + str(a_list))
for index, elem in enumerate(a_list):
    if(index+1 < len(a_list)):
     sum = elem + a_list[index+1]
     print (sum)
    



