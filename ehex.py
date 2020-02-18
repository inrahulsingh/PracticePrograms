def ask():
    while True:
        try:
            x=int(input("Input an integer\n"))
            y=x**2
        except:
            print("An error occured, please try again\n")
            continue
        else:
            print("Thank you, your number squared is: ", y)
            break
        
