#CH8_Part_3

phrase = 'In space, no one can hear you code.'
my_list = ['B', 'n', 'n', '5']
cargo_hold = "water,space suits,food,plasma sword,batteries"

# The split and list methods convert a string into a list, while the join method does the opposite.

# See what happens when you print phrase.split() vs. phrase.split('e') vs. list(phrase). What is the purpose of the argument inside the ()?
print(phrase.split())

# See what happens when you print ''.join(my_list) vs. 'a'.join(my_list) vs. '_'.join(my_list). What is the purpose of the argument inside the ()?
print(''.join(my_list))

# Split the cargo_hold string at each comma, alphabetize the list with sort, then combine the elements into a new string. Use a hyphen to join the elements together in the string.
cargo_hold = cargo_hold.split(',')
cargo_hold.sort()
cargo_hold = '-'.join(cargo_hold)
print(cargo_hold)

# Do split, list, or join change the original string/list?
    #No they do not