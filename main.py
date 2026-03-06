num1 = int(input(">> "))
num2 = int(input(">> "))

operation_list = ['+', '-', '*', '/']

print('Choose operation number: ')
for x in range(len(operation_list)):
    print(f'{x + 1} - {operation_list[x]}')
operation_num = int(input(">> "))

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

