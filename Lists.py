# Initialize and print a list. Note that lists can be
# Text, Numbers, or a combination of many data types.
 
#Todo = ["Take out garbage", "Study Essentials", "Write python program for Mo"]
#print(Todo)
 
#NumLst = [3, 6, 3, 7, 2, 9]
#print(NumLst)
'''
MixedLst = [15, 38.54, "Text too", 58, 2, True, 3.14159]
print(MixedLst)
EmptyList = []
 
 
 
# To add a value to the end of a list, use the append method.
 
Todo.append("Buy da partner flowers")
print(Todo)
 
 
# print the values in a list using a loop.
 
print()
for Job in Todo:
    print(Job)
 
 
# print the values from a list and number them.
JobNum = 1
print()
for Job in Todo:
    print(f"{str(JobNum)}. {Job}")
    JobNum += 1
 
 
# Delete a value from a list.
 
UserDel = int(input("Enter the job number to delete: "))
Todo.__delitem__(UserDel-1)
# Note that you can also use ToDo.pop() to remove the last item.
 
# Just printing out the list again to show the delete worked.
 
JobNum = 1
print()
for Job in Todo:
    print("{}. {}".format(str(JobNum), Job))
    JobNum += 1
 
 
# Add values to a list until the user enters 0 to stop.
 
NumLst = []
while True:
    Number = int(input("Enter a number (0 to end): "))
    if Number == 0:
        break
    NumLst.append(Number)
 
# Print the list to show all the numbers are included.
 
print()
print(NumLst)
 
print()
for Number in NumLst:
    print(Number)
'''
   
 
# Validate use input ising a list of values.
 
ProvLst = ["NL", "NS", "PE", "NB"]
while True:
    Prov = input("Enter the province (XX): ").upper()
    if Prov == "":
        print("Error - Province cannot be blank - Please reenter.")
    elif len(Prov) != 2:
        print("Error - Province is a 2 digit code - please reenter.")
    elif Prov not in ProvLst:
        print("Error - Not a valid province - please reenter.")
    else:
        break
 
print("Province has been successfully entered.")






