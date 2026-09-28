catMarks=int(input("Enter your cat marks:"))
examMarks=int(input("Enter your exam marks:"))
sum=catMarks+examMarks
if(sum>=70):
    print("You have passed, you have an A")
    print("Move to year 3")
elif(sum>=60):
    print("You have a B")
    print("Move to year 3")
elif(sum>=50):
    print("You have a C")
    print("Move to year 3")
elif(sum>=40):
    print("You have a D")
    print("Move to year 3")
else:
    print("You have an E")
    print("You have faied")


#2 ways decision
remarks = "Passed" if (sum>=40) else "Failed"
print(remarks)