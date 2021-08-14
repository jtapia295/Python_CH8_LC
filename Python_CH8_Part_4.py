# Webpage = https://education.launchcode.org/lchs/chapters/lists/exercises.html

# Not enough comments? Add your own to explain what your code is doing!

# Code Part 1a here:
    #Define and assign the following lists, which hold the name, chemical symbol and mass for different elements:
element_1 = ['hydrogen', 'H', 1.008]
element_2 = ['helium', 'He', 4.003]
element_26 = ['iron', 'Fe', 55.85]


# Code Part 1b here:
#Define the list table, and use table.append(list_name) to add each of the element lists to it. 
# Print table to see its structure.
table = []
table.append(element_1),table.append(element_2),table.append(element_26)
print(table)

# Code Part 1c here:
#Use bracket notation to examine the difference between printing table[1] and table[1][1]. 
print(table[1])
print(table[1][1])
# Don’t just nod your head! I want to HEAR you describe this difference. 
# Go ahead, talk to your screen.

# Code Part 1d here:
    #Using bracket notation and the table list, print the mass from element_1, 
    #the name from element_2, and the symbol from element_26.
print(table[0][2],table[1][0],table[2][1])

# Code Part 2 here:
#Now create a 3-dimensional list. A good mental model is to think of a filing cabinet.

#Define at least four, 1-dimensional lists. Call each one a folder. For example:
folder_1 = ['page_1', 'page_2', 'page_3', 'page_4']
folder_2 = ['page_5','page_6','page_7','page_8']
folder_3 = ['page_9','page_10','page_11','page_12']
folder_4 = ['page_13','page_14','page_15','page_16']
#Now define at least two, 2-dimensional lists. Call these lists drawers. 
#Each element in a drawer is one of the folders. For example:
drawer_1 = [folder_1, folder_2]
drawer_2 =  [folder_3,folder_4]
#Now define one 3-dimensional cabinet list. Each element is one of the 2-D drawer lists.
cabinet = [drawer_1, drawer_2]

#Experiment! Print out one entry from each level in the cabinet list.
print(cabinet)
print('<-------------------->')
print(cabinet[0])
print('<-------------------->')
print(cabinet[1][0])
print('<-------------------->')
print(cabinet[0][1][1])
print('<-------------------->')
