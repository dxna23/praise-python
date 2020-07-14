again = "yes"
while again == "yes":
    praiseType = input("Select a type of praise \n a: personality \n b: appearance \n c: intelligence")

    if praiseType  == "a":
        print ("You are an interesting person")
    elif praiseType == "b":
        print ("You look good")
    elif praiseType == "c":
        print ("You are smart")
        
    else:
        print ("That wasn't an option")

    again = input( "Would you like some more praise?")
    
