#Part1 
# #N.1
adding_practice = [273.15]
print(adding_practice)

adding_practice.append(42),adding_practice.append('hello')
print(adding_practice)

#N.2
second_list =  [False,-4.6,'87']
new_list = adding_practice + second_list

print(new_list)


cargo_hold_list = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']
cargo_hold_list.insert(cargo_hold_list.index('slinky'), 'Space Tether'),cargo_hold_list.remove('slinky')  
print(cargo_hold_list)