while True:
    num1 = input("Enter a number: ")
    if num1 == 'q':
        break
    num2 = input("Enter a second number: ")
    if num2 == 'q':
        break

    try:
        num = int(num1) + int(num2)
    except ValueError:
        print("Must use numbers only")
    else:
        print(num)

