exit = True
while exit:
    x = int(input("Type your 1st number : "))
    logical_op = """
+ = 1
- = 2
* = 3
/ = 4"""
    print(logical_op)
    print()
    logical_op_in = int(input("Select option : "))
    print()
    if logical_op_in == 1:
        y = int(input("Type your 2nd number : "))
        print()
        logical_op = x + y
        print(x,"+",y,"=",logical_op)
    elif logical_op_in == 2:
        y = int(input("Type your 2nd number : "))
        print()
        logical_op = x - y
        print(x,"-",y,"=",logical_op)
    elif logical_op_in == 3:
        y = int(input("Type your 2nd number : "))
        print()
        logical_op = x * y
        print(x,"*",y,"=",logical_op)
    elif logical_op_in == 4:
        y = int(input("Type your 2nd number : "))
        print()
        logical_op = x/y
        print(x,"/",y,"=",logical_op)
    else:
        print("!!Wrong selection!!")
    task = str.lower(input("Do you want to continue : YES/NO : "))
    if task != "yes":
        print()
        print("Have a great day!!")
        quit()
    else:
        print()         
    
