# print text at end using keyword "end"
print("hello", "world", end=" !!\n")

# multi line print without new line
print("hello", "world", end=" ")
print("this", "is", end=" ")
print("my", "first program", end = " !!\n")


# print text using custom separator
print("hello", "world", sep="--", end=" !!")

# print text using multiplier
print("hello", "world"*2, sep="--", end=" !!")

# print text using formatter, separator and end keywords
fname=input("enter first name: ")
lname=input("enter last name: ")

print("fname: %s" %(fname), "lname: %s" %(lname), sep="-", end=" !!\n")
print("fname: {}, lname: {}".format(fname, lname)*3, sep="//", end=" !!\n")
