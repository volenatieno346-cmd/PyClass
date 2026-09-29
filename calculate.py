
mathProblem=input("Enter your math problem: ")
temp=[]
x= ""
y=[]
sign="+-*/"
usedSign=None
for ch in mathProblem:
    if ch.isdigit():
        x += ch
    elif ch in sign:
        if x != "":
            temp.append(int(x))
            x=""
            usedSign = ch
        else:
            temp.append(ch)
            continue

if x != "":
    temp.append(int(x))

if len(temp) == 2 and usedSign is not None:
    if usedSign == "+":
        result = temp[0] + temp[1]
    elif usedSign == "-":
        result = temp[0] - temp[1]
    elif usedSign == "*":
        result = temp[0] * temp[1]
    elif usedSign == "/":
        result = temp[0] / temp[1]
    else:
        result = "Invalid operator"

print("The numbers in the problem are: ", result)