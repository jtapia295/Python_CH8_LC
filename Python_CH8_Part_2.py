#Part 2
cargo_hold_list = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

#Use slices to make the following changes to the final cargo_hold list from part 1. Be sure to print the list after each step to confirm your work.
    
    #Insert the string 'keys' at index 3 without replacing any other entries.
cargo_hold_list[3:3] = 'keys',
print(cargo_hold_list)
    
    #Remove 'instruction manual' from the list. (Hint: The index method is helpful to avoid manually counting an index).
print('<---------------->')
cargo_index = cargo_hold_list.index('instruction manual')
print(cargo_index)
cargo_hold_list[cargo_index:cargo_index +1] = ''
print(cargo_hold_list)


    #Replace the elements at indexes 2 - 4 with the items 'cat', 'book', and 'string cheese'.
print('<---------------->')
cargo_hold_list[2:4] = 'cat', 'book' , 'string cheese'
print(cargo_hold_list)
   
    #Some methods—like append and pop—alter the original list, while others do not. Use the lists
    #to see if taking a slice or using the reverse and sort methods changes the original list.
supplies_1 = ['duct tape', 'gum', 3.14, False, 6.022e23]
supplies_2 = ['orange drink', 'nerf toys', 'camera', '42', 'Rutabaga']

#Print a slice of the last 3 items from supplies_1. Does slice alter the original list? Verify this by printing supplies_1 after taking the slice.

print('<------------------------>')
print(supplies_1[-3:])
print(supplies_1)

#Reverse the first list, sort the second, and then print both lists. What is the difference between the two methods?
print('<------------------------>')
supplies_1.reverse()
supplies_2.sort()

print(supplies_1,supplies_2)

#Do reverse or sort alter the original lists?
    #They do not change the memory location though they do change the ordering



