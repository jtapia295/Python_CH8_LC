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


#N.3
#A
cargo_hold_list = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']
cargo_hold_list.insert(cargo_hold_list.index('slinky'), 'Space Tether'),cargo_hold_list.remove('slinky')  
print(cargo_hold_list)

print('<---------------->')

#B
cargo_hold_list.pop(-1)
print(cargo_hold_list)

print('<---------------->')

#C
print(f'Index to be removed: {cargo_hold_list[0]}')
cargo_hold_list.pop(0)
print(cargo_hold_list)

print('<---------------->')

#D
cargo_hold_list.append(1138),cargo_hold_list.append('20 Meters')
print(cargo_hold_list)

print('<---------------->')

#E
cargo_hold_list.remove('parrot')
print(cargo_hold_list)

#F
print(f'The list Cargo Hold contains {len(cargo_hold_list)} items.')