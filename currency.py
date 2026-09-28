currency = input("Enter your currency:(in upper case) ")

amount =float(input("enter amount: "))
warning= " a valid amount" if(amount>0 ) else "invalid Amount"
if (amount>0):
    match currency:
        case "USD" :print(amount*130,"KSH")
        
        case "CSD" :print(amount*93, "KSH")

        case "EUROS" :print(amount*148, "KSH")

        case "UG":print(amount*0.033, "KSH")

        case "TZ":print(amount/0.048, "KSH")
else:
    print()
