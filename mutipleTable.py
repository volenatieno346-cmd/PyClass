number=int(input("Enter a number you want to form the multiplication table for: "))
for i in range(number, 0, -1):
    for j in range(number, 0, -1):
        print(i * j, end="\t")
    print("\n")