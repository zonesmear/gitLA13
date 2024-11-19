print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Exit")

choice = ""

while choice.upper() != 'D':
    choice = input("ENTER SELECTION [A, B, C, or D]: ")

    if choice.upper() == 'A':
        print("Add Record")
        addRec()
    elif choice.upper() == 'B':
        print("View Records")
        viewRec()
    elif choice.upper() == 'C':
        print("Clear All Records")
        clearRec()
    elif choice.upper() == 'D':
        print("Thank you!")
    else:
        print("Invalid selection! Please choose A, B, C, or D.")
        
def addRec():
    file = open(filename, 'r')
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    addr = input("Enter Address: ")
    with open(filename, 'a') as file:
        file.write(name + ", " + email + ", " + addr + "\n")
    file.close()