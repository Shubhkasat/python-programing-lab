from easygui import *
import sys

while 1:
    msgbox("Welcome to e bazar")

    msg ="In which category you want to buy items?"
    title = "amazon"
    choices=["Smartphones", "Clothes", "Stationary",]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Smartphones":
        msgbox("Welcome to Smartphone bazaar")
        msg="Which Smartphone?"
    	title= "amazon"
    	choices= [" 1---price=100000", " 2---price=200000", "3---price=300000", " 4---price---400000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at amazon")
    elif choice=="Clothes":
        msgbox("Welcome to Clothes bazaar")
        msg="What type of clothes?"
    	title= "amazon"
    	choices= ["Shirt Mens-M size-----Rs 500","Shirt Women-M size-----Rs 500","Jeans Pant forMens-----Rs1000","Jeans Pant for Women-----Rs1000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")


        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at amazon")
    elif choice=="Stationary":
        msgbox("Welcome to Stationary bazaar")
        msg="Choose your item?"
    	title="amazon"
    	choices= ["Parker Pens Special Edition pack of 5 ---- price=Rs10000 ", "Scissors Pack of 10----- price=Rs500"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to deliver at your default address)?"
        title = "Please Confirm"
        msgbox("Thank you for buying at amazon")

    if ccbox(msg, title):    
        pass  
    else:
        sys.exit(0)
