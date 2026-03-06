def is_num(x: str) -> bool:
    try:
        int(x)
        return true
    except:
        return false

checker_num = false
while g:
    n1 = input(">> ")
    t = is_num(n1)
    n2 = input(">> ")
    t1 = is_num(n2)
    g = (t and t1)

num1 = int(n1)
num2 = int(n2)

operation_list = ['+', '-', '*', '/']
checker_oper = false 
while checker_oper:
    print('Choose operation number: ')
    for x in range(len(operation_list)):
        print(f'{x + 1} - {operation_list[x]}')
    oper = input(">> ")
    checker_oper = is_num(oper)
operation_num = int(oper)

if operation_num == 1:
    pass
elif operation_num == 2:
    pass
elif operation_num == 3:
    print(f'{num1} * {num2} = {num1 * num2}')
elif operation_num == 4:
    if num2 <= 0:
        print(f"Error: {num2} <= 0")
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
else:
    print("Error: operation not found!")

