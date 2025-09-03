import calc1

calculate = ["sum", "diff", "multi", "divide", "pow", "sqrt", 
             "prime", "least com multi", "int divide", "per cent" ]

while True:
    print(calculate)
    print("")
    oper = input("Please enter a mathematical operation from the list above: ")
    if oper not in calculate:
        oper = input("Invalid input. Please try again: ")
    elif oper == calculate[0]:
        try:
            a = float(input("Enter the first number: "))
        except ValueError:
            a = 0
        try:
            e = float(input("Enter the second number: "))
        except ValueError:
            e = 0
        try:
            i = float(input("Enter the third number(or simply press enter to input nothing): "))
        except ValueError:
            i = 0
        try:
            o = float(input("Enter the third number(or simply press enter to input nothing): "))
        except ValueError:
            o = 0
        print(f"The sum is {calc1.calc_sum(a, e, i, o)}.")
            

    elif oper == calculate[1]:
        try:
            a = float(input("Enter the first number: "))
        except ValueError:
            a = 0
        try:
            e = float(input("Enter the second number: "))
        except ValueError:
            e = 0
        print(f"The difference is {calc1.calc_diff(a, e)}.")
    
    elif oper == calculate[2]:
        try:
            a = float(input("Enter the first number: "))
        except ValueError:
            a = 1
        try:
            e = float(input("Enter the second number: "))
        except ValueError:
            e = 1
        try:
            i = float(input("Enter the third number(or simply press enter to input nothing): "))
        except ValueError:
            i = 1
        try:
            o = float(input("Enter the third number(or simply press enter to input nothing): "))
        except ValueError:
            o = 1
        print(f"The result of the multiplication is {calc1.calc_multi(a, e, i, o)}.")
    
    elif oper == calculate[3]:
        try:
            a = float(input("Enter the first number: "))
        except ValueError:
            a = 1
        try:
            e = float(input("Enter the second number: "))
        except ValueError:
            e = 1
        print(f"The result of the division is {calc1.calc_div(a, e)}.")
    
    elif oper == calculate[4]:
        try:
            a = float(input("Enter the first number: "))
        except ValueError:
            a = 1
        try:
            e = float(input("Enter the second number: "))
        except ValueError:
            e = 1
        print(f"{a} to the power of {e} is {calc1.calc_pow(a, e)}.")
    
    elif oper == calculate[5]:
        try:
            a = float(input("Enter a number: "))
        except ValueError:
            a = 1
        print(f"The square root of {a} is {calc1.calc_root(a)}.")
    
    elif oper == calculate[6]:
        try:
            a = int(input("Enter a whole number: "))
        except ValueError:
            a = 1
        print(calc1.calc_prime(a))
    
    elif oper == calculate[7]:
        try:
            a = int(input("Enter the first number(whole numbers only): "))
        except ValueError:
            a = 1
        try: 
            e = int(input("Enter the second number(whole numbers only): "))
        except ValueError:
            e = 1
        try:
            i = int(input("Enter the third number(or simply press enter to input nothing): "))
        except ValueError:
            i = 1
        if i != 1:
            print(f"The least common multiple of {a}, {e} and {i} is {calc1.calc_lcm(a, e, i)}.")
        else:
            print(f"The least common multiple of {a} and {e} is {calc1.calc_lcm(a, e, i)}.")
        
    elif oper == calculate[8]:
        try:
            a = int(input("Enter the first number(whole numbers only): "))
        except ValueError:
            a = 1
        try:
            e = int(input("Enter the second number(whole numbers only): "))
        except ValueError:
            e = 1
        print(calc1.calc_intdiv(a, e))
    
    elif oper == calculate[9]:
        try:
            a = float(input("Enter the smaller number(whole numbers only): "))
        except ValueError:
            a = 1
        try:
            e = float(input("Enter the larger number(whole numbers only): "))
        except ValueError:
            e = 1
        print(f"{a} is {calc1.calc_pcent(a, e)}% of {e}.")
