firstnumber = int(input("Введи первое число: "))
secondnumber = int(input("Введи второе число: "))

oper = input("Введите действие: ")

operations=["+","-","*","/","//","%","**",">","<",">=","<=","==","!="]

if oper not in operations:
    print( "Неверное действие")
    
func = False
if secondnumber == 0:
    func = True

if oper in operations:
    if oper =="+":
        print(firstnumber+secondnumber)
    elif oper == "-":
        print(firstnumber-secondnumber)
    elif oper == "*":
        print(firstnumber*secondnumber)
    elif oper == "/" and not func != False:
        print(firstnumber/secondnumber)
    elif oper == "//" and not func != False:
        print(firstnumber//secondnumber)
    elif oper == "%" and not func != False:
        print(firstnumber%secondnumber)
    elif oper == "**":
        print(firstnumber**secondnumber)
    elif oper == "==":
        print (firstnumber is secondnumber)
    elif oper == "!=":
        print(firstnumber is not secondnumber)
    elif oper == ">":
        print(firstnumber>secondnumber)
    elif oper == "<":
        print(firstnumber<secondnumber)
    elif oper == "<=":
        if firstnumber < secondnumber or firstnumber == secondnumber:
            print(True)
        else:
            print(False)
    elif oper == ">=":
        if firstnumber>secondnumber or firstnumber==secondnumber:
            print(True)
        else:
            print(False)

    else:
        print ("Error")
