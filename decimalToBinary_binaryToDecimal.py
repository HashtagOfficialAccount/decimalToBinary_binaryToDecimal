while True:
    print("d - decimal to binary; b - binary to decimal; q - quit\n")
    option = input("Enter one of the options above: ").strip().lower()
    if option == "d":
        num = int(input("Enter decimal value to convert to binary: \n").strip())
        start = num
        rem = 0
        binary = []
        while True:
            rem = start % 2
            start = start//2
            if start == 0:
                binary.insert(0,rem)
                break
            else:
                binary.insert(0,rem)
        answer = ""
        for i in binary:
            answer += str(i)
        print(f"{num} in binary is {answer}\n")
    elif option == "b":
        binary = input("Enter binary value to convert to decimal: \n").strip()
        start = 2**(len(binary) - 1)
        decimal = 0
        for i in binary:
            if i == "1":
                decimal += start
            start = start/2
        print(f"{binary} in decimal is {decimal}\n")
    elif option == "q":
        break
    else:
        print("That wasn't an option\n")

