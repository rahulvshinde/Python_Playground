# initialize list 
test_list = ['gfg', 'is', 'best', "for", 'CS', 'and', 'Maths' ] 
  
# initialize split list 
split_list = [('gfg', 'best'), ('CS', 'Maths')] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# printing split list  
print("The split list is : " + str(split_list)) 
  
# Splitting string list by strings 
# using loop + index() + list slicing 
for start, end in split_list: 
        print("Start {}, End {}".format(start,end))
        temp1 = test_list.index(start) 
        temp2 = test_list.index(end) + 1
        print(temp1, temp2)
        test_list[temp1 : temp2] = [test_list[temp1 : temp2]] 
  
# printing result 
print("The resultant split list is : " + str(test_list)) 
