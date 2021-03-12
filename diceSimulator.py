import random
print("This is a dice")
x = "y"

while (x == "y"):
    
    number = random.randint(1,6)

    if number == 1:
        print("-----------")
        print("|         |")
        print("|    *    |")
        print("|         |")
        print("-----------")
    if number == 2:
        print("-----------")
        print("| *       |")
        print("|         |")
        print("|       * |")
        print("-----------")
    if number == 3:
        print("-----------")
        print("| *       |")
        print("|    *    |")
        print("|       * |")
        print("-----------")
    if number == 4:
        print("-----------")
        print("| *     * |")
        print("|         |")
        print("| *     * |")
        print("-----------")
    if number == 5:
        print("-----------")
        print("| *     * |")
        print("|    *    |")
        print("| *     * |")
        print("-----------")
    if number == 6:
        print("-----------")
        print("| *     * |")
        print("| *     * |")
        print("| *     * |")
        print("-----------")
    x = input("Press y to roll again. Press n to finish: ")
