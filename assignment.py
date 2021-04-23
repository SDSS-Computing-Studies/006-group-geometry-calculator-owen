#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

main()

def maintitle():
    #This will display a title screen
    #Input parameter: None needed
    #Output parameter: None
    #Author: Obliz
    title = "Mini Cube Calculator"
    print(title)
    return None

def mainmenuA():
    #This will display the first insturction
    #Input parameter: None needed
    #Output parameter: None
    #Author: Obliz
    menu1 = "\nThis calculator will calculate 5 aspects of a cube:"
    menu2 = "\n-The area of the cube. \n-The volume of the cube. \n-The are of one face of the cube. \n-The diagonal of one face of the cube. \n-The solid diagonal."
    print(menu1)
    print(menu2)
    return None

def mainmenuB():
    #This will display the second instruction
    #Input parameter: None needed
    #Output parameter: None
    #Author: Obliz
    menu3 = "\nEnter 1,2,3,4 or 5 to commit the corresponded calculation:"
    menu4 = "1 is for calculating the area. \n2 is for calculating the volmue. \n3 is for the are of a face. \n4 is for the diagonal of a face. \n5 is for the solid diagonal."
    menu5 = "When the questions appear, please enter an approriate value."
    print(menu3)
    print(menu4)
    print(menu5)
    return None

def Aofcube(side):
    area = 6*(side*side)
    return area

def Vofcube(side):
    volume = side*side*side
    return volume

def Aofface(side):
    facearea = side*side
    return facearea

def diagonal(side):
    diaofface = (2*(side*side))**(1/2)
    return diaofface

def soliddiagonal(side):
    soliddia = (((2*(side*side))**(1/2)) + side**2)**(1/2)
    return soliddia

def mainstream():
    #This will run the program and control it's flow
    #The program will ask for a value and it will calculate the corresonded calculation
    #Ther calculation repeats until the user chooses to exit
    #Author: Obliz
    maintitle()
    mainmenuA()
    mainmenuB()
    
    quit = False

    while quit == False:
        option = input("Do you wish to continue? Enter \"yes\" to continue or \"no\" to exit: ")
        if option == "yes":
            side = float(input("What is the length of the side: ")) #input length of side
            calc = int(input("Which calculation do you wish to commit: "))
            if calc == 1:
                Aofcube(side)
                print("The area of the cube is:", Aofcube(side))
            elif calc == 2:
                Vofcube(side)
                print("The volume of the cube is:", Vofcube(side))
            elif calc == 3:
                Aofface(side)
                print("The area of a face of the cube is:", Aofface(side))
            elif calc == 4:
                diagonal(side)
                print("The diagonal of a face of the cube is:", diagonal(side))
            elif calc == 5:
                soliddiagonal(side)
                print("The solid diagonal of the cube is:", soliddiagonal(side))
        elif option == "no":
            print("Closing Program") #Closes Program
            quit = True
        else:
            print("An Error Has Occured") #Error
            mainmenuB()

mainstream()