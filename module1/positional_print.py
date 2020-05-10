print("Hello World, my first python script")
print('Printing names.....')

fname=input("enter first name: ")
lname=input("enter last name: ")

# print using arg replacement, option 1
print('first name is {}'.format(fname))
# print using arg replacement, option 2
print("last name is %s" %(lname))

# print using multiple arg replacement, option 1
print('{} {}'.format(fname, lname))
# print using multiple arg replacement, option 2
print('%s %s' %(fname, lname))

# print using multiple arg replacement with dbl quotes, option 1
print("{} {}".format(fname, lname))
# print using multiple arg replacement with dbl quotes, option 2
print("%s %s" %(fname, lname))


print()
print('''Multi line print
%s
%s
''' %(fname, lname))
