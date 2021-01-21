def fun(num, ls):
    secNum = 0
    while num != 0:
        secNum += (num % 10) ** 2
        num = int(num / 10)

    print(secNum)

    if secNum == 1:
        print("The number is happy")
        exit()

    for i in ls:
        if i == secNum:
            print("The number is not happy")
            exit()
    ls.append(secNum)

    fun(secNum, ls)


def main():
    ls = []
    num = int(input("Enter the number to be checked"))
    fun(num, ls)


if __name__ == "__main__":
    main()