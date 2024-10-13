#function to allow the user to buy the protective phone case
def procase(y):
    z= ("false")
    print("which type of case do you want?")
    print("1) a rubber case, for $20")
    print("2) a carbon fibre case, for $100")
    while z== "false":
        x= input("enter your preffered phone case: ")
        if x == ("1"):
            print("")
            print("amazing! you have selected the rubber case")
            z=("true")
            return y+20
        elif x==("skip"):
            z=("true")
            print("")
            print("you have chosen to skip this option")
            return y
        elif x == ("2"):
            print("")
            print("awesome! you have selected the carbon fibre case") 
            y=y+100
            return y
            z=("true")
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")
#function to allow the user to buy the battery charger
def batterycharger(y):
    z = ("false")
    print("do you want an extra fast battery charger for $100?")
    print("1) yes")
    print("2) no")
    while z ==("false"):
        x=input("enter your choice about a battery charger: ")
        if x == ("1") or x == ("yes") or x == ("y"):
            print("")
            print("fantastic! you have chosen to purchase an extra fast battery charger")
            z=("true")
            return y+100
        elif x==("2") or x==("skip")or x==("no")or x==("n"):
            print("")
            print("you have chosen to skip this option")
            z=("true")
            return y
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")
#function which allows the user to trade in their old phones
def oldphone(y):
    z=("false")
    print("would you like to trade in your old phone to recieve a discount of $40 on your purchase?")
    print("1) yes")
    print("2) no")
    while z==("false"):
        x = input("enter your choice about a phone trade in: ")
        if x == ("1") or x == ("yes") or x == ("y"):
            print("")
            print("good! you have chosen to trade in your old phone")
            z=("true")
            return y-40
        elif x==("2") or x==("skip")or x==("no")or x==("n"):
            print("")
            print("you have chosen to skip this option")
            z=("true")
            return y
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")
#function to determine in the customer wants monthly phone insurance
def phoneinsurance(w,y):
    z=("false")
    print("would you like to purchase montly insurance for your phone for a price of $",w,"a month?")
    print("1) yes")
    print("2) no")
    while z==("false"):
        x = input("enter your choice about phone insurance: ")
        if x == ("1") or x == ("yes") or x == ("y"):
            print("")
            print("spectacular! you have chosen to purchase phone insurance")
            z=("true")
            return y+w
        elif x==("2") or x==("skip")or x==("no")or x==("n"):
            print("")
            print("you have chosen to skip this option")
            z=("true")
            return y
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")
#function to determine the purchase of a monthly data plan
def dataplan(y):
    z= ("false")
    print("which data plan do you want?")
    print("1) 1GB a month, for $10 a month")
    print("2) 2GB a month, for $15 a month")
    print("3) 5GB a month, for $40 a month")
    print("4) 20 GB a month, for $150 a month")
    while z== "false":
        x= input("enter your preffered data plan: ")
        if x == ("1"):
            print("")
            print("incredible! you have selected 1GB per month plan")
            z=("true")
            return y+10
        elif x==("skip"):
            z=("true")
            print("")
            print("you have chosen to skip this option")
            return y
        elif x == ("2"):
            print("")
            print("incredible! you have selected the 2GB per month plan") 
            return y+15
        elif x==("3"):
            print("")
            print("incredible, you have selected the 5GB per month plan")
            z=("true")
            return y+40
        elif x==("4"):
            print("")
            print("incredible! you have selected the 20GB per month plan")
            return y+150
        else:
            print("please only enter the number '1', '2', '3', or '4', or the word 'skip'")
#function to print the final totals
def finish(x,y):
    print ("thank you for choosing to shop at Ian's Phone Shop.")
    print("your final total is $",x,", which you will pay upfront")
    if y >= 1:
        print("you will also now have a monthly bill of $",y,", which will be billed to you later this week")
    print("have a good day!")
#function to find extra storage options
def storageoptions(y):
    z= ("false")
    print("which additional storage option do you want?")
    print("1) an additional 64GB, for $200")
    print("2) an additional 128GB, for $350")
    while z== "false":
        x= input("enter your preffered storage option: ")
        if x == ("1"):
            print("")
            print("amazing! you have selected the additional 64GB")
            z=("true")
            return y+200
        elif x==("skip"):
            z=("true")
            print("")
            print("you have chosen to skip this option")
            return y
        elif x == ("2"):
            print("")
            print("awesome! you have selected the additional 128GB") 
            y=y+350
            return y
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")
#function to allow cloud data backup
def clouddata(y):
    print("which Cloud Data Backup length is best suited for you?")
    print("1) cloud data backup for 1 year, which costs $20")
    print("2) cloud data backup for 2 years, which costs $35")
    z=("false")
    while z==("false"):
        x= input("enter your preffered option: ")
        if x == ("1"):
            print("")
            print("congragulations! you have selected one years of cloud data backup")
            p=input("please enter your email address for the cloud data backup to be linked to: ")
            z=("true")
            return y+20
        elif x==("skip"):
            z=("true")
            print("")
            print("you have chosen to skip this option")
            return y
        elif x == ("2"):
            print("")
            print("congragulations! you have selected two years of cloud data backup") 
            p=input("please enter your email address for the cloud data backup to be linked to: ")
            return y+35
        else:
            print("please only enter the number '1' or '2', or the word 'skip'")

monthlytotal=0
total=0
actualoptioncheck=("false")
print ("welcome to Ian's mobile phone shop. Today we are offering three packages:")
print ("1) the McBasic package, which costs $50 and has 2GB of phone storage included")
print ("2) the Average Joe package, which costs $150 and has 8GB of phone storage included")
print ("3) the Rich Kid Pro package, which costs $800 and has 32GB of phone storage included")
print ("please select which package you want by entering the number at the start of your prefered choice, for example, if you wanted the McBasic package, enter '1'")
print ('\033[1m'+"if you want to skip an option throughout this process, please enter 'skip'")
while actualoptioncheck==("false"):
    decisionpackage = input('\033[0m'+"enter Your Preferred Phone Package: ")
    if decisionpackage == ("1"):
        print("")
        print("great! you selected the McBasic package.")
        total = total+50
        total = procase(total)
        total=batterycharger(total)
        monthlytotal=phoneinsurance(1,monthlytotal)
        monthlytotal=dataplan(monthlytotal)
        total=oldphone(total)
        finish(total,monthlytotal)
        actualoptioncheck=("true")
    elif decisionpackage == ("2"):
        print("")
        print("great! you selected the Average Joe Package")
        total= total+150
        total=storageoptions(total)
        total=clouddata(total)
        total = procase(total)
        total=batterycharger(total)
        monthlytotal=phoneinsurance(5,monthlytotal)
        monthlytotal=dataplan(monthlytotal)
        total=oldphone(total)
        finish(total,monthlytotal)
        actualoptioncheck=("true")


    elif decisionpackage==("3"):
        print("")
        print("great! you selected the Rich Kid Pro package")
        total=total+800
        total=storageoptions(total)
        print("would you like to purchase extra diamonds for $200")
        print("1) yes")
        print("2) no")
        diamondcheck=("false")
        while diamondcheck==("false"):
            diamond = input("enter your choice about extra diamonds: ")
            if diamond == ("1") or diamond == ("yes") or diamond == ("y"):
                print("")
                print("spectacular! you have chosen to purchase extra diamonds")
                diamondcheck=("true")
                total=total+200
            elif diamond==("2") or diamond==("skip")or diamond==("no")or diamond==("n"):
                print("")
                print("you have chosen to skip this option")
                diamondcheck=("true")
            else:
                print("please only enter the number '1' or '2', or the word 'skip'")
        total=clouddata(total)
        total=procase(total)
        total=batterycharger(total)
        monthlytotal=phoneinsurance(20,monthlytotal)
        monthlytotal=dataplan(monthlytotal)
        total=oldphone(total)
        finish(total,monthlytotal)
        actualoptioncheck=("true")


    elif decisionpackage==("skip"):
        print("")
        total=procase(total)
        total=batterycharger(total)
        monthlytotal=dataplan(monthlytotal)
        total=oldphone(total)
        finish(total,monthlytotal)
        actualoptioncheck=("true")
    else:
        print("please only enter the numbers '1', '2', or '3', or the word 'skip'")
