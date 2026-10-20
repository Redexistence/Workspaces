x = 120
def fun1():
    """This function prints 1"""
    print(1)

def fun2():
    """This function prints 2"""
    print(2)

def ModifyVal():
    global x
    x += 200
    print(x)

def main():
    fun1()
    fun2()
    print(fun1().__doc__)
    print(fun2().__doc__)
    print(x)
    print(ModifyVal())
    print(x)

if __name__ == "__main__":
    main()